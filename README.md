# UGotIt - LangChain ReAct Agent

一个基于 LangChain 的 ReAct 智能代理，支持多种工具调用和自定义技能扩展。

## 功能特点

- 🤖 使用 DeepSeek API 作为 LLM 后端
- 🔧 内置文件系统操作工具（创建、读取、更新、删除文件）
- 💻 支持执行系统命令
- 📝 可通过 Markdown 文件扩展自定义技能
- 🧠 对话记忆功能（保留最近 10 轮对话）
- 🌐 专为 Windows 系统优化

## 项目结构

```
ugotit/
├── agent.py              # 核心 Agent 实现
├── main.py               # 主程序入口
├── tool_loader.py        # Markdown 技能加载器
├── tools/                # 内置工具模块
│   ├── __init__.py
│   ├── file_system.py    # 文件系统工具
│   └── shell.py          # Shell 命令工具
├── skills/               # 自定义技能目录
│   └── open_browser.md   # 示例技能
├── test/                 # 测试和验证代码
│   ├── __init__.py
│   └── ...
├── .gitignore
├── requirements.txt      # 依赖列表
├── Pipfile
└── Pipfile.lock
```

## 安装步骤

### 1. 克隆或下载项目

```bash
cd ugotit
```

### 2. 创建虚拟环境（推荐）

使用 Pipenv：
```bash
pip install pipenv
pipenv install
pipenv shell
```

或者使用 pip：
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

在项目根目录创建 `.env` 文件，添加以下内容：

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_MODEL=deepseek-chat
DEEPSEEK_API_BASE=https://api.deepseek.com
```

请将 `your_deepseek_api_key_here` 替换为您的 DeepSeek API 密钥。

## 使用方法

### 启动程序

```bash
python main.py
```

### 交互示例

启动后，您可以与 Agent 进行对话：

```
欢迎使用 Langchain ReAct Agent!
您可以输入 'exit' 来退出程序。
可用工具:
  - create_file: 创建一个新文件并写入内容。
  - read_file: 读取文件的内容。
  - update_file: 向现有文件追加内容。
  - delete_file: 删除一个文件。
  - run_shell_command: 执行一个系统命令并返回其输出。
  - open_browser: 打开浏览器访问指定网址。

请输入您的指令: 创建一个名为 hello.txt 的文件，内容是 Hello World!
```

输入 `exit` 可以退出程序。

## 内置工具

### 文件系统工具

- `create_file(file_path, content)` - 创建文件
- `read_file(file_path)` - 读取文件
- `update_file(file_path, content)` - 追加内容到文件
- `delete_file(file_path)` - 删除文件

### Shell 工具

- `run_shell_command(command)` - 执行系统命令

## 自定义技能

您可以通过在 `skills/` 目录下添加 Markdown 文件来扩展自定义技能。

### 技能文件格式示例 (`skills/open_browser.md`)

```markdown
---
name: open_browser
description: 打开浏览器访问指定网址
---
```shell
start {{input}}
```
```

### 技能文件说明

1. **YAML 元数据块**（必须）：
   - `name`: 技能名称（必须是有效的 Python 标识符）
   - `description`: 技能描述

2. **Shell 命令块**（必须）：
   - 使用 `{{input}}` 作为用户输入的占位符
   - 命令执行后会返回输出结果

## 测试

项目包含多个测试文件，位于 `test/` 目录下。

运行最终测试：
```bash
python test/final_test.py
```

## 技术栈

- **LangChain**: Agent 框架
- **LangChain-OpenAI**: OpenAI 兼容 LLM 接口
- **LangChain-Classic**: 传统 Agent 实现
- **Python-Dotenv**: 环境变量管理
- **DeepSeek API**: 大语言模型服务

## 注意事项

1. 确保已正确配置 `.env` 文件
2. 本项目专为 Windows 系统设计，Shell 命令会使用 Windows 语法
3. 执行系统命令时请谨慎操作

## 许可证

MIT License
