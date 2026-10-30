# SPaRE

**Scattering-Prior-Aware Representation Enhancement for Fine-Grained SAR Vehicle Recognition**

[English](README.md) | [接口展示](demo/) | [公开数据入口](data/README.md)

## 项目介绍

SPaRE 面向单通道幅度图像的细粒度 SAR 车辆识别，将幅度派生的散射先验、任务特征细化和局部响应组织相结合。

框架包含无类别标签的散射先验学习（LSPL）、先验引导特征细化（PGFR）和目标分量结构学习（TCSL）。
LSPL 在不使用类别及语义部件标签的条件下学习散射相关参考；PGFR 利用冻结参考细化任务特征；
TCSL 将局部响应组织为用于分类的分量上下文。

本仓库提供项目介绍、输入输出接口演示和官方数据资源入口。

## 接口演示

```bash
python demo/interface_demo.py
```

该脚本使用 Python 标准库，打印示意性的输入描述和输出格式，用于展示接口，不执行模型推理。
示例中的张量尺寸仅用于说明。详见[接口说明](demo/README.md)。

## 数据

数据请通过 [ATRNet-STAR 官方项目](https://github.com/waterdisappear/ATRNet-STAR) 获取，
协议说明见 [ATRBench](https://github.com/waterdisappear/ATRNet-STAR/blob/main/ATRBench/README.md)。
数据使用条件及引用要求以数据作者的说明为准。

## 许可

接口示例采用 [MIT 许可](LICENSE)。第三方数据集及其他资源遵循各自的许可与使用条款。
