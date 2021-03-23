class Clock {

	constructor( autoStart ) {

		this.autoStart = ( autoStart !== undefined ) ? autoStart : true;

		this.startTime = 0;
		this.oldTime = 0;
		this.elapsedTime = 0;

		this.running = false;

	}

	start() {

		this.startTime = now();

		this.oldTime = this.startTime;
		this.elapsedTime = 0;
		this.running = true;

	}

	stop() {

		this.getElapsedTime();
		this.running = false;
		this.autoStart = false;

	}

	getElapsedTime() {

		this.getDelta();
		return this.elapsedTime;

	}

	getDelta() {

		let diff = 0;

		if ( this.autoStart && ! this.running ) {

			this.start();
			return 0;

		}

		if ( this.running ) {

			const newTime = now();

			diff = ( newTime - this.oldTime ) / 1000;
			this.oldTime = newTime;

			this.elapsedTime += diff;

		}

		return diff;

	}

}

function now() {

	return ( typeof performance === 'undefined' ? Date : performance ).now(); // see #10732

}


class Model3D {
    constructor() {
        this.scene = undefined;
        this.params = undefined;
        this.clock = new Clock();
    }
    load(scene, params) {
        this.scene = scene;
        this.params = params;
        this._load(scene, params);
    }
    move(elapsedTime) {
        if (this.scene == undefined)
            return;
        this._move(elapsedTime);
    }
}

class Drone extends Model3D {
    constructor() {
        super();
        this.speed = {x: -0.1, y: -0.005, z: 0};
        this.dAngle = {x: 0.005, y: 0, z: 0};
        this.angle = {x: 0, y: 0, z: 0};
        this.props = [];
        this.signs = [-1, -1, 1, 1];
        this.PROP_ROTATION_SPEED = 0.2;

        // Mouse movement stuff
        this.mouse = new THREE.Vector2();
        this.plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0);
        this.raycaster = new THREE.Raycaster();
        this.intersectPoint = new THREE.Vector3();

        this.STATES = {
            start: 0,
            takeoff: 1,
            hover1: 2,
            hover2: 3,
            hover3: 4,
            flying: 5,
            crash: 6,
            out: 7,
            flipStart: 8,
            flipMiddle: 9,
            idle: 10,
            rollStart: 11,
            rollMiddle: 12,
            rollFinish: 13,
            spinStart: 14,
            spinMiddle: 15,
        };
    }

    _load(scene, params) {
        for (let i = 0; i < 4; i++) {
            this.props[i] = scene.getObjectByName(`props${i+1}`);
        }

        window.addEventListener('mousemove', e => this.onMouseMove(e));

        this.startpos = new THREE.Vector3(window.innerWidth / 64, 20, 0);
        this.startRot = new THREE.Vector3(0, 0, 0);

        this.scene.position.set(this.startpos.x, this.startpos.y, this.startpos.z);
        this.scene.scale.set(3, 3, 3);
        this.clock.start();

        this.state = this.STATES.idle;
        this.counter = 0;
    }

    onMouseMove(e) {
        if (this.state != this.STATES.idle)
            return;

        this.mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
        this.mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

        this.raycaster.setFromCamera(this.mouse, this.params.camera);//set raycaster
        this.raycaster.ray.intersectPlane(this.plane, this.intersectPoint); // find the point of intersection
        this.scene.lookAt(this.intersectPoint); // face our arrow to this position
        this.scene.rotateY(Math.PI/2+.3);
    }

    flip() {
        this.scene.rotation.z = 0;
        this.state = this.STATES.flipStart;
    }
    roll() {
        this.scene.rotation.set(this.startRot.x, this.startRot.y, this.startRot.z);
        this.state = this.STATES.rollStart;
    }
    spin() {
        this.state = this.STATES.spinStart;
    }

    _move(elapsedTime) {

        switch (this.state) {
            case this.STATES.start:
                this.scene.position.set(0, 0, 10);
                this.scene.rotation.set(0, Math.PI/2, 0);
                if (this.clock.getElapsedTime() > 1) {
                    this.state = this.STATES.flying;
                }
                break;
            case this.STATES.takeoff:
                this.scene.translateY(.05);
                if (this.scene.position.y > 5) {
                    this.state = this.STATES.hover1;
                    this.clock.start();
                }
                break;
            case this.STATES.flipStart:
                this.prevPos = new THREE.Vector3(this.scene.position.x, this.scene.position.y, this.scene.position.z);
                this.scene.translateX(-100 * elapsedTime);
                this.scene.rotateZ(-100 * elapsedTime);
                this.state = this.STATES.flipMiddle;
                break;
            case this.STATES.flipMiddle:
                if (Math.abs(this.scene.rotation.z) < 0.1) {
                    this.state = this.STATES.idle;
                }
                this.scene.translateX(-400 * elapsedTime);
                this.scene.rotateZ(-40 * elapsedTime);
                break;
            case this.STATES.rollStart:
                this.scene.rotateX(0.11);
                this.state = this.STATES.rollMiddle;
                break;
            case this.STATES.rollMiddle:
                if (Math.abs(this.scene.rotation.x) < 0.1)
                    this.state = this.STATES.rollFinish;
                else
                    this.scene.rotateX(.1);
                break;
            case this.STATES.spinStart:
                this.scene.rotation.set(this.startRot.x, this.startRot.y, this.startRot.z);
                this.count = 0;
                this.scene.rotateY(0.11);
                this.state = this.STATES.spinMiddle;
                break;
            case this.STATES.spinMiddle:
                if (Math.abs(this.scene.rotation.y) < 0.05) {
                    if (this.count == 0) {
                        this.scene.rotateY(.1);
                        this.count++;
                    } else {
                        this.state = this.STATES.rollFinish;
                    }
                } else {
                    this.scene.rotateY(.1);
                }
                break;
            case this.STATES.rollFinish:
                this.scene.rotation.set(this.startRot.x, this.startRot.y, this.startRot.z);
                this.state = this.STATES.idle;
            case this.STATES.idle:
                this.scene.position.set(this.startpos.x, this.startpos.y, this.startpos.z);
                break;
        }

        this.rotateProps();
    }

    rotateProps() {
        for (let i = 0; i < 4; i++) {
            this.props[i].rotation.y -= this.signs[i] * this.PROP_ROTATION_SPEED;
        }
    }
}

class Car extends Model3D {
    constructor() {
        super();
        this.speed = 200 + Math.random() * 200;
        this.wheels = [0, 0, 0, 0];
    }

    _load(scene) {
        for (let i = 0; i < 4; i++) {
            this.wheels[i] = this.scene.getObjectByName(`wheel${i+1}`);
        }
        this.scene.scale.set(1.5, 1.5, 1.5);
        this.setPos();
    }

    setPos() {
        this.scene.position.set(
            -40 + 100*Math.random(),
            -10,
            -400 + 150*Math.random());
    }

    _move(elapsedTime) {
        for (let wheel of this.wheels) {
            wheel.rotateY(20 * elapsedTime);
        }
        this.scene.translateZ(this.speed * elapsedTime);
        if (this.scene.position.z > 40) {
            this.setPos();
        }
    }

}