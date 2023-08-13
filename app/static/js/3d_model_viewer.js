var scene, camera, renderer, controls;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('modelPreview').appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.25;
    controls.enableZoom = true;
}

function loadModel(fileUrl) {
    var loader = new THREE.STLLoader();
    loader.load(fileUrl, function (geometry) {
        var material = new THREE.MeshPhongMaterial({color: 0xff5533, specular: 0x111111, shininess: 200});
        var mesh = new THREE.Mesh(geometry, material);

        mesh.position.set(0, -0.25, 0);
        mesh.rotation.set(0, -Math.PI / 2, 0);
        mesh.scale.set(0.5, 0.5, 0.5);

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        scene.add(mesh);
        animate();
    });
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

window.onload = init;