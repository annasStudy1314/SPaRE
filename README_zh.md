# SPaRE

**Scattering-Prior-Aware Representation Enhancement for Fine-Grained SAR Vehicle Recognition**

[English](README.md) | [接口说明](demo/README.md) | [公开数据入口](https://github.com/waterdisappear/ATRNet-STAR)

## 项目介绍

SPaRE 面向单通道幅度图像的细粒度 SAR 车辆识别，将幅度派生的散射先验、任务特征细化和局部响应组织相结合。

| 模块 | 功能 |
| --- | --- |
| 无类别标签的散射先验学习（LSPL） | 不使用类别及语义部件标签，学习散射相关参考。 |
| 先验引导特征细化（PGFR） | 利用冻结参考细化任务特征。 |
| 目标分量结构学习（TCSL） | 将局部响应组织为用于分类的分量上下文。 |

本仓库提供项目介绍、输入输出接口演示和官方数据资源入口。

## 快速开始

环境要求：Python 3.9 或以上。接口演示不需要安装第三方包，也不需要 GPU、数据集或模型权重。
在仓库根目录执行：

```bash
python demo/interface_demo.py
python demo/interface_demo.py --output interface_description.json
```

脚本校验示例并打印 JSON 格式的接口描述；使用 `--output` 可将描述保存为文件。
示例输入形状为 `[1, 1, 128, 128]`，类别分数的示意形状为 `[1, 40]`。
这是接口演示，不执行模型推理，也不生成预测分数或识别结果。详见[接口说明](demo/README.md)。

## 目录导航

| 路径 | 内容 |
| --- | --- |
| [demo/](demo/) | 命令行接口演示、JSON 示例与字段说明 |
| [code/](code/) | 演示代码入口说明 |
| [data/](data/) | 官方数据集及评估协议链接 |
| [tests/](tests/) | 接口校验与命令行测试 |

## 接口测试

```bash
python -m unittest discover -s tests -v
```

测试涵盖字段与尺寸校验、命令行运行、JSON 导出、无效输入及输入文件覆盖保护。
这些测试用于检查演示接口，不代表模型识别性能评测。

## 数据

数据请通过 [ATRNet-STAR 官方项目](https://github.com/waterdisappear/ATRNet-STAR) 获取，
协议说明见 [ATRBench](https://github.com/waterdisappear/ATRNet-STAR/blob/main/ATRBench/README.md)。
数据使用条件及引用要求以数据作者的说明为准。

## 许可

接口示例采用 [MIT 许可](LICENSE)。第三方数据集及其他资源遵循各自的许可与使用条款。
