const canvas = document.getElementById('3d-canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45,
                            window.innerWidth / window.innerHeight,
                            0.1, 1000);
camera.position.x = 0;
camera.position.y = 0;
camera.position.z = 50;

const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true
});
renderer.setSize( window.innerWidth, window.innerHeight);

// Add lighting
const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(10, 10, 10);
scene.add(light);

const controls = new THREE.OrbitControls(camera, renderer.domElement);