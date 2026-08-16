# 四冲程柴油机 · 高精度 3D 交互仿真（本地复刻）

复刻自 https://diesel-engine-3d.pages.dev/ 的**单文件静态站点**，已完全本地化，可离线运行。

## 技术栈
- 原生 HTML/CSS/JS（无框架、无打包构建）
- Three.js `0.160.0`（ES Module，已下载到 `vendor/`）
- 3D 引擎**全程序化生成**（圆柱/方块/管道几何 + 运动学方程），无外部 GLB/纹理/音频/接口

## 文件结构
```
diesel-engine-3d/
├── index.html                       # 全部 DOM + 内联 CSS + 内联 module 脚本（仅改了 importmap）
├── vendor/
│   ├── three.module.js             # Three.js 0.160.0 build
│   └── addons/
│       ├── controls/OrbitControls.js
│       └── environments/RoomEnvironment.js
└── README.md
```

## 与原站差异（仅一处）
原站通过 importmap 从 jsdelivr CDN 加载 Three.js：
```json
"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
"three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
```
复刻版改为本地相对路径：
```json
"three":"./vendor/three.module.js",
"three/addons/":"./vendor/addons/"
```
其余 CSS、几何、运动学、UI、粒子流逻辑**原样保留**，未作任何改写。

## 启动方式
ES Module + importmap 需经 HTTP 提供（`file://` 直接打开会被浏览器拦截）：

```bash
cd diesel-engine-3d
python3 -m http.server 8123
# 浏览器打开 http://127.0.0.1:8123
```

## 功能
- 直列四缸柴油机 · 四冲程 · 发火顺序 1-3-4-2
- 转速 / 负荷滑块、启动、停机手动盘车、观察倍率（×1 / ×0.2 / ×0.05）
- 零件悬浮信息卡（名称/材料/功能/参数/实时状态）
- 剖视模式、自由/侧/俯/前端视角预设
- 冷却/润滑/进气/排气 粒子流（流量随转速/负荷变化）
- 气门启闭相位、实时水温/油压/增压、fps

## 限制
无。所有资源已内联或本地化，断网亦可运行。
