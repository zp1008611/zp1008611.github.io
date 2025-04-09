# 模拟仿真环境技术栈概述

## Reference

- https://articulatedrobotics.xyz/tutorials/
- https://blog.csdn.net/qq_44732054/category_12109258.html
- https://webthesis.biblio.polito.it/26714/1/tesi.pdf
- https://www.bilibili.com/video/BV1dH4y137ZR/?spm_id_from=333.788&vd_source=3d4b12fb4a4bfbc98942d43612ae2fb9
- https://www.yuque.com/xtdrone/manual_cn/basic_config

## Gazebo和AirSim

Gazebo 和 AirSim 是两个用于模拟环境的工具，但它们的用途和特点有所不同：

### Gazebo
1. **用途**：主要用于机器人模拟和测试，支持多种机器人平台。
2. **功能**：提供物理引擎、传感器模拟、3D环境建模等功能。
3. **集成**：与 ROS（Robot Operating System）集成良好，适合于机器人开发和研究。
4. **场景**：用户可以创建复杂的场景，并模拟机器人在这些场景中的行为。

6. **性能**：
   - 通常对计算资源的需求较低，尤其是在简单场景中。
   - 物理引擎（如 ODE、Bullet）相对轻量，适合实时仿真。

7. **计算资源**：
   - 可以在较低配置的计算机上运行，适合嵌入式系统或资源有限的设备。
   - 多机器人仿真时，资源占用可能增加，但可以通过简化模型和场景来优化。

### AirSim
1. **用途**：专注于无人机和自动驾驶汽车的仿真。
2. **功能**：提供高保真的视觉效果和传感器模拟（如相机、激光雷达等）。
3. **集成**：与 Unreal Engine 集成，支持高质量的图形和物理效果。
4. **场景**：提供城市环境和自然环境的模拟，适合于自动驾驶和无人机飞行的研究。

5. **性能**：
   - 对计算资源的需求较高，特别是在高保真图形和复杂环境下。
   - 使用 Unreal Engine 提供高质量的视觉效果，可能导致更高的帧率要求。

6. **计算资源**：
   - 需要较强的 GPU 支持，以实现流畅的图形渲染和物理模拟。
   - 在资源有限的设备上运行时，可能会遇到性能瓶颈。

### 总结
- **Gazebo** 更加侧重于机器人领域的应用，适合多种机器人类型的开发。但比较轻量，适合资源有限的环境。
- **AirSim** 主要面向无人机和自动驾驶汽车，强调视觉效果和现实感。但是需要更高的计算能力，适合追求高保真度的应用场景。选择时应考虑目标平台的硬件配置和应用需求。


## XTDrone

## sjtu_drone

https://github.com/NovoG93/sjtu_drone
