# SPaRE 项目预览

[English](README.md) | [接口展示](demo/) | [公开数据入口](data/README.md)

本仓库目前仅提供论文投稿前的项目介绍、输入输出格式示例，以及公开数据集链接。
**核心算法实现暂不公开。**

公开范围：

- 简要项目说明。
- 合成输入的元信息和示意性输出格式。
- ATRNet-STAR 与 ATRBench 官方页面链接。

不公开模型内部结构代码、训练流程、代理标签生成算法、超参数配方、权重或实验记录。
仓库不是完整开源实现，也不是论文实验复现包。

```bash
python demo/interface_demo.py
```

该脚本仅打印格式说明，不读取真实图像、不加载模型、不执行识别，也不生成准确率。

数据请通过 [ATRNet-STAR 官方项目](https://github.com/waterdisappear/ATRNet-STAR) 获取，
协议说明见 [ATRBench](https://github.com/waterdisappear/ATRNet-STAR/blob/main/ATRBench/README.md)。
数据使用条件及引用要求以数据作者的说明为准。

本仓库的 MIT 许可仅覆盖当前公开的小型接口示例，不覆盖未公开的核心代码、数据、权重或论文。
