# AgentUniverse 项目结构说明

AgentUniverse 是一个智能代理（Agent）框架，以下是项目主要目录结构及其功能说明：

## 核心目录

### /agent
Agent 的核心实现目录，包含：
- 智能代理的基础类实现（agent.py）
- 代理管理器（agent_manager.py）
- 输入输出对象定义
- 代理模型定义
- 多个专门子目录：
  - action/: 代理可执行的动作实现
  - memory/: 代理记忆/历史管理
  - plan/: 代理规划模块
  - work_pattern/: 工作模式定义
  - template/: 代理模板
  - default/: 默认实现

主要依赖：
- langchain_core: 用于可运行序列化和配置
- abc: 用于抽象基类定义
- typing: 类型注解支持
- datetime: 时间处理
- threading: 线程支持
- uuid: 唯一标识符生成

### /llm
大语言模型（LLM）集成模块，支持：
- OpenAI
- Claude
- Wenxin (文心)
- Ollama
等多种 LLM 实现，包含：
- LLM 管理器
- 各种 LLM 实例的具体实现
- LangChain 集成实现

主要依赖：
- tiktoken: 用于令牌计数
- langchain_core: LLM 基础模型支持
- abc: 抽象基类定义
- typing: 类型注解
- pydantic: 数据验证和设置管理

### /workflow
工作流管理模块，负责：
- 工作流定义和执行
- 节点管理
- 工作流图结构
- 工作流输出处理

主要依赖：
- networkx: 图结构处理
- typing: 类型注解
- pydantic: 数据模型定义

### /prompt
提示词（Prompt）管理模块，包含：
- 提示词模型定义
- 聊天提示词实现
- 提示词管理器
- 提示词枚举定义

主要依赖：
- pydantic: 数据模型和验证
- typing: 类型注解
- enum: 枚举类型支持

### /base
框架基础模块，包含：
- 核心框架实现（agentuniverse.py）
- 上下文管理（context/）
- 工具类（util/）
- 注解定义（annotation/）
- 组件管理（component/）
- 配置管理（config/）

主要依赖：
- pydantic: 配置管理
- typing: 类型系统
- logging: 日志管理
- toml: 配置文件解析

### /database
数据库操作模块，提供：
- SQL 数据库包装器
- 数据库管理器

主要依赖：
- sqlalchemy: 数据库 ORM
- typing: 类型注解
- pydantic: 数据模型

### /agent_serve
服务层实现，包含：
- 服务配置
- 服务实例管理
- Web 服务实现
- 服务管理器

主要依赖：
- fastapi: Web 服务框架
- pydantic: 数据验证
- uvicorn: ASGI 服务器
- typing: 类型注解

## 项目特点
1. 模块化设计：各个功能模块清晰分离
2. 可扩展性：支持多种 LLM 集成
3. 完整工作流：从代理定义到服务部署的完整支持
4. 灵活配置：提供丰富的配置选项和管理机制

## 核心依赖包
1. langchain-core: LLM 应用开发框架
2. pydantic: 数据验证和设置管理
3. fastapi: Web 服务框架
4. sqlalchemy: 数据库 ORM
5. tiktoken: Token 计数工具
6. networkx: 图结构处理
7. toml: 配置文件处理

## 版本要求
- Python >= 3.9
- pydantic >= 2.6.4, < 2.7.0
- langchain-core >= 0.1.0
- fastapi >= 0.100.0
