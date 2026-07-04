# Engine API reality-check (anti-hallucination)

Codex builds these games from memory of the engine APIs, which is where **hallucinated methods**
creep in — plausible names borrowed from another engine or an old version (e.g. `MathUtils.lerpAngle`,
which is Unity's `Mathf.LerpAngle`, **not** three.js). This file is the ground truth for the pinned
versions so you can *look up* an API instead of *recalling* it.

**Pinned versions:** three.js **r0.185.1** · Phaser **3.90.0**. Everything below was extracted from
those exact releases' source.

## The three rules

1. **Don't invent APIs.** You are on three.js r0.185.1 and Phaser 3.90.0 — only use methods that
   exist in *those* versions. No methods from Unity, Godot, p5.js, GSAP, or a newer/older version.
2. **Hand-write math helpers; don't trust convenience methods.** Core primitives are safe and
   well-known (`Vector3`, `Quaternion.slerp`, `Math.sin/atan2`, `MathUtils.lerp/clamp/damp`). The
   *convenience* helpers are where hallucinations live. For anything beyond a core primitive, write
   the 2–3 lines yourself (snippets below) — you can't hallucinate an API you don't call.
3. **Verify before you use it.** Before calling any engine helper you're not 100% sure of, grep this
   file:
   ```bash
   grep -wi lerpAngle "${PLUGIN_ROOT}/references/engine-apis.md"   # not found = don't use it
   ```
   If it's not here (and isn't a core primitive), either hand-write it or confirm it in the pinned
   source (`raw.githubusercontent.com/mrdoob/three.js/r185/…`, `…/phaserjs/phaser/v3.90.0/…`) —
   **do not guess.** three.js *addons* (OrbitControls, GLTFLoader) are NOT in the core list below;
   they live under `three/addons/…` (examples/jsm) — verify their names there. The Phaser lists
   below are the top-level namespaces + the most hallucination-prone method sets, not every method
   of every class; for a deep instance method, check the pinned source.

## Common cross-engine / stale-version traps

| Hallucinated | Reality in the pinned version |
|---|---|
| `THREE.MathUtils.lerpAngle` | ❌ doesn't exist (that's Unity). Use the `lerpAngle` snippet below. |
| `THREE.MathUtils.smoothDamp` / `moveTowards` | ❌ don't exist. Use `MathUtils.damp` or the snippets below. |
| `THREE.Math.*` | ❌ renamed — it's `THREE.MathUtils.*`. |
| `new THREE.Geometry()` | ❌ removed years ago — only `BufferGeometry` exists. |
| `new THREE.SphereBufferGeometry()` (and `Box/Plane…BufferGeometry`) | ❌ the `*BufferGeometry` names were removed — use `SphereGeometry`, `BoxGeometry`, … |
| `Phaser.Math.Lerp(a,b,t)` | ❌ it's **`Phaser.Math.Linear(a, b, t)`**. |
| angle lerp in Phaser | use `Phaser.Math.Angle.RotateTo` / `Phaser.Math.Angle.Wrap` / `Phaser.Math.Angle.ShortestBetween`. |
| `this.add.<x>` for a made-up object | check the `this.add.*` list below — if it's not there, it's not a factory method. |

## Ready-made plain-JS helpers (paste instead of guessing)

```js
const clamp      = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
const lerp       = (a, b, t) => a + (b - a) * t;               // three.js: MathUtils.lerp / Phaser: Math.Linear
const invLerp    = (a, b, v) => (v - a) / (b - a);             // three.js: MathUtils.inverseLerp
// Frame-rate-independent smoothing toward a target (three.js MathUtils.damp is the real one):
const expDecay   = (a, b, lambda, dt) => b + (a - b) * Math.exp(-lambda * dt);
// Angle lerp the short way around the circle — three.js has NO lerpAngle:
const lerpAngle  = (a, b, t) => a + (((b - a + Math.PI) % (Math.PI * 2)) - Math.PI) * t;
// Step toward a target by at most maxStep:
const moveTowards = (a, b, maxStep) => Math.abs(b - a) <= maxStep ? b : a + Math.sign(b - a) * maxStep;
```

## Greppable API surfaces (extracted from the pinned releases)

Grep these before using an engine symbol. Present = real in this version; absent = don't use it
(hand-write it or check the pinned source / addons path).

### three.js r185 — `THREE.MathUtils.*` (the usual hallucination site)

```
ceilPowerOfTwo clamp damp degToRad denormalize euclideanModulo floorPowerOfTwo 
generateUUID inverseLerp isPowerOfTwo lerp mapLinear normalize pingpong radToDeg 
randFloat randFloatSpread randInt seededRandom setQuaternionFromProperEuler 
smootherstep smoothstep 
```

### three.js r185 — all top-level `THREE.*` exports (core; addons are separate)

```
ACESFilmicToneMapping AddEquation AddOperation AdditiveAnimationBlendMode 
AdditiveBlending AgXToneMapping AlphaFormat AlwaysCompare AlwaysDepth AlwaysStencilFunc 
AmbientLight AnimationAction AnimationClip AnimationLoader AnimationMixer 
AnimationObjectGroup AnimationUtils ArcCurve ArrayCamera ArrowHelper AttachedBindMode 
Audio AudioAnalyser AudioContext AudioListener AudioLoader AxesHelper BackSide 
BasicDepthPacking BasicShadowMap BatchedMesh BezierInterpolant Bone 
BooleanKeyframeTrack Box2 Box3 Box3Helper BoxGeometry BoxHelper BufferAttribute 
BufferGeometry BufferGeometryLoader ByteType Cache Camera CameraHelper CanvasTexture 
CapsuleGeometry CatmullRomCurve3 CineonToneMapping CircleGeometry ClampToEdgeWrapping 
Clock Color ColorKeyframeTrack ColorManagement Compatibility CompressedArrayTexture 
CompressedCubeTexture CompressedTexture CompressedTextureLoader ConeGeometry 
ConstantAlphaFactor ConstantColorFactor Controls CubeCamera CubeDepthTexture 
CubeReflectionMapping CubeRefractionMapping CubeTexture CubeTextureLoader 
CubeUVReflectionMapping CubicBezierCurve CubicBezierCurve3 CubicInterpolant 
CullFaceBack CullFaceFront CullFaceFrontBack CullFaceNone Curve CurvePath 
CustomBlending CustomToneMapping CylinderGeometry Cylindrical Data3DTexture 
DataArrayTexture DataTexture DataTextureLoader DataUtils DecrementStencilOp 
DecrementWrapStencilOp DefaultLoadingManager DepthFormat DepthStencilFormat 
DepthTexture DetachedBindMode DirectionalLight DirectionalLightHelper 
DiscreteInterpolant DodecahedronGeometry DoubleSide DstAlphaFactor DstColorFactor 
DynamicCopyUsage DynamicDrawUsage DynamicReadUsage EdgesGeometry EllipseCurve 
EqualCompare EqualDepth EqualStencilFunc EquirectangularReflectionMapping 
EquirectangularRefractionMapping Euler EventDispatcher ExternalTexture ExtrudeGeometry 
FileLoader Float16BufferAttribute Float32BufferAttribute FloatType Fog FogExp2 
FramebufferTexture FrontSide Frustum FrustumArray GLBufferAttribute GLSL1 GLSL3 
GreaterCompare GreaterDepth GreaterEqualCompare GreaterEqualDepth 
GreaterEqualStencilFunc GreaterStencilFunc GridHelper Group HTMLTexture HalfFloatType 
HemisphereLight HemisphereLightHelper IcosahedronGeometry ImageBitmapLoader ImageLoader 
ImageUtils IncrementStencilOp IncrementWrapStencilOp InstancedBufferAttribute 
InstancedBufferGeometry InstancedInterleavedBuffer InstancedMesh Int16BufferAttribute 
Int32BufferAttribute Int8BufferAttribute IntType InterleavedBuffer 
InterleavedBufferAttribute Interpolant InterpolateBezier InterpolateDiscrete 
InterpolateLinear InterpolateSmooth InterpolationSamplingMode InterpolationSamplingType 
InvertStencilOp KeepStencilOp KeyframeTrack LOD LatheGeometry Layers LessCompare 
LessDepth LessEqualCompare LessEqualDepth LessEqualStencilFunc LessStencilFunc Light 
LightProbe Line Line3 LineBasicMaterial LineCurve LineCurve3 LineDashedMaterial 
LineLoop LineSegments LinearFilter LinearInterpolant LinearMipMapLinearFilter 
LinearMipMapNearestFilter LinearMipmapLinearFilter LinearMipmapNearestFilter 
LinearSRGBColorSpace LinearToneMapping LinearTransfer Loader LoaderUtils LoadingManager 
LoopOnce LoopPingPong LoopRepeat MOUSE Material MaterialBlending MaterialLoader 
MathUtils Matrix2 Matrix3 Matrix4 MaxEquation Mesh MeshBasicMaterial MeshDepthMaterial 
MeshDistanceMaterial MeshLambertMaterial MeshMatcapMaterial MeshNormalMaterial 
MeshPhongMaterial MeshPhysicalMaterial MeshStandardMaterial MeshToonMaterial 
MinEquation MirroredRepeatWrapping MixOperation MultiplyBlending MultiplyOperation 
NearestFilter NearestMipMapLinearFilter NearestMipMapNearestFilter 
NearestMipmapLinearFilter NearestMipmapNearestFilter NeutralToneMapping NeverCompare 
NeverDepth NeverStencilFunc NoBlending NoColorSpace NoNormalPacking NoToneMapping 
NormalAnimationBlendMode NormalBlending NormalGAPacking NormalRGPacking NotEqualCompare 
NotEqualDepth NotEqualStencilFunc NumberKeyframeTrack Object3D ObjectLoader 
ObjectSpaceNormalMap OctahedronGeometry OneFactor OneMinusConstantAlphaFactor 
OneMinusConstantColorFactor OneMinusDstAlphaFactor OneMinusDstColorFactor 
OneMinusSrcAlphaFactor OneMinusSrcColorFactor OrthographicCamera PCFShadowMap 
PCFSoftShadowMap PMREMGenerator Path PerspectiveCamera Plane PlaneGeometry PlaneHelper 
PointLight PointLightHelper Points PointsMaterial PolarGridHelper PolyhedronGeometry 
PositionalAudio PropertyBinding PropertyMixer QuadraticBezierCurve 
QuadraticBezierCurve3 Quaternion QuaternionKeyframeTrack QuaternionLinearInterpolant 
R11_EAC_Format RED_GREEN_RGTC2_Format RED_RGTC1_Format REVISION RG11_EAC_Format 
RGBADepthPacking RGBAFormat RGBAIntegerFormat RGBA_ASTC_10x10_Format 
RGBA_ASTC_10x5_Format RGBA_ASTC_10x6_Format RGBA_ASTC_10x8_Format 
RGBA_ASTC_12x10_Format RGBA_ASTC_12x12_Format RGBA_ASTC_4x4_Format RGBA_ASTC_5x4_Format 
RGBA_ASTC_5x5_Format RGBA_ASTC_6x5_Format RGBA_ASTC_6x6_Format RGBA_ASTC_8x5_Format 
RGBA_ASTC_8x6_Format RGBA_ASTC_8x8_Format RGBA_BPTC_Format RGBA_ETC2_EAC_Format 
RGBA_PVRTC_2BPPV1_Format RGBA_PVRTC_4BPPV1_Format RGBA_S3TC_DXT1_Format 
RGBA_S3TC_DXT3_Format RGBA_S3TC_DXT5_Format RGBDepthPacking RGBFormat RGBIntegerFormat 
RGB_BPTC_SIGNED_Format RGB_BPTC_UNSIGNED_Format RGB_ETC1_Format RGB_ETC2_Format 
RGB_PVRTC_2BPPV1_Format RGB_PVRTC_4BPPV1_Format RGB_S3TC_DXT1_Format RGDepthPacking 
RGFormat RGIntegerFormat RawShaderMaterial Ray Raycaster RectAreaLight RedFormat 
RedIntegerFormat ReinhardToneMapping RenderTarget RenderTarget3D RepeatWrapping 
ReplaceStencilOp ReverseSubtractEquation RingGeometry SIGNED_R11_EAC_Format 
SIGNED_RED_GREEN_RGTC2_Format SIGNED_RED_RGTC1_Format SIGNED_RG11_EAC_Format 
SRGBColorSpace SRGBTransfer Scene ShaderChunk ShaderLib ShaderMaterial ShadowMaterial 
Shape ShapeGeometry ShapePath ShapeUtils ShortType Skeleton SkeletonHelper SkinnedMesh 
Source Sphere SphereGeometry Spherical SphericalHarmonics3 SplineCurve SpotLight 
SpotLightHelper Sprite SpriteMaterial SrcAlphaFactor SrcAlphaSaturateFactor 
SrcColorFactor StaticCopyUsage StaticDrawUsage StaticReadUsage StereoCamera 
StreamCopyUsage StreamDrawUsage StreamReadUsage StringKeyframeTrack SubtractEquation 
SubtractiveBlending TOUCH TangentSpaceNormalMap TetrahedronGeometry Texture 
TextureLoader TextureUtils Timer TimestampQuery TorusGeometry TorusKnotGeometry 
Triangle TriangleFanDrawMode TriangleStripDrawMode TrianglesDrawMode TubeGeometry 
UVMapping Uint16BufferAttribute Uint32BufferAttribute Uint8BufferAttribute 
Uint8ClampedBufferAttribute Uniform UniformsGroup UniformsLib UniformsUtils 
UnsignedByteType UnsignedInt101111Type UnsignedInt248Type UnsignedInt5999Type 
UnsignedIntType UnsignedShort4444Type UnsignedShort5551Type UnsignedShortType 
VSMShadowMap Vector2 Vector3 Vector4 VectorKeyframeTrack VideoFrameTexture VideoTexture 
WebGL3DRenderTarget WebGLArrayRenderTarget WebGLCoordinateSystem WebGLCubeRenderTarget 
WebGLRenderTarget WebGLRenderer WebGLUtils WebGPUCoordinateSystem WebXRController 
WireframeGeometry WrapAroundEnding ZeroCurvatureEnding ZeroFactor ZeroSlopeEnding 
ZeroStencilOp createCanvasElement error getConsoleFunction log setConsoleFunction warn 
warnOnce 
```

### Phaser 3.90 — top-level `Phaser.*` namespaces

```
Actions Animations BlendModes Cache Cameras Class Core Create Curves DOM Data Display 
Events FX Game GameObjects Geom Input Loader Math Physics Plugins Renderer Scale 
ScaleModes Scene Scenes Structs Textures Tilemaps Time Tweens Utils 
```

### Phaser 3.90 — `Phaser.Math.*`

```
Angle Average Bernstein Between CatmullRom CeilTo Clamp DegToRad Difference Distance 
Easing Euler Factorial FloatBetween FloorTo FromPercent Fuzzy GetSpeed Interpolation 
IsEven IsEvenStrict Linear LinearXY Matrix3 Matrix4 MaxAdd Median MinSub Percent Pow2 
Quaternion RadToDeg RandomDataGenerator RandomXY RandomXYZ RandomXYZW Rotate 
RotateAround RotateAroundDistance RotateTo RotateVec3 RoundAwayFromZero RoundTo 
SinCosTableGenerator SmoothStep SmootherStep Snap ToXY TransformXY Vector2 Vector3 
Vector4 Within Wrap 
```

### Phaser 3.90 — `Phaser.Math.Angle.*`

```
Between BetweenPoints BetweenPointsY BetweenY CounterClockwise GetClockwiseDistance 
GetCounterClockwiseDistance GetShortestDistance Normalize Random RandomDegrees Reverse 
RotateTo ShortestBetween Wrap WrapDegrees 
```

### Phaser 3.90 — `Phaser.Geom.*`

```
Circle Ellipse Intersects Line Mesh Point Polygon Rectangle Triangle 
```

### Phaser 3.90 — `Phaser.GameObjects.*` (classes)

```
Arc BitmapText Blitter Bob BuildGameObject BuildGameObjectAnimation Components 
Container Creators Curve DOMElement DisplayList DynamicBitmapText Ellipse Events Extern 
Factories GameObject GameObjectCreator GameObjectFactory GetCalcMatrix GetTextSize 
Graphics Grid Group Image IsoBox IsoTriangle Layer Line MeasureText Particles 
PathFollower Polygon Rectangle RenderTexture RetroFont Rope Shape Sprite Star 
StaticBitmapText Text TextStyle TileSprite Triangle UpdateList Video Zone 
```

### Phaser 3.90 — scene factory `this.add.*` (GameObjectFactory)

```
arc bitmapMask bitmapText blitter circle container curve dom dynamicBitmapText ellipse 
extern follower graphics grid group image isobox isotriangle layer line mesh nineslice 
particles path plane pointlight polygon rectangle renderTexture rope shader sprite star 
text tileSprite tilemap timeline triangle tween tweenchain video zone 
```

### Phaser 3.90 — `Phaser.Physics.Arcade.*` and `this.physics.add.*` (Arcade Factory)

```
Namespace: ArcadePhysics Body Collider Components Events Factory GetCollidesWith 
GetOverlapX GetOverlapY Group Image SeparateX SeparateY Sprite StaticBody StaticGroup 
Tilemap World 
Arcade factory (this.physics.add.): body collider group image overlap sprite staticBody 
staticGroup staticImage staticSprite 
```
