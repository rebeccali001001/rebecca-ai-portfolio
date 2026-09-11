# Reinforcement Learning

## Module/Topic/Source File

- Module: 01 · AI Foundations
- Topic: Reinforcement Learning
- Source File: `reinforcement-learning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Reinforcement Learning | 强化学习 | A method where an agent learns what to do from rewards and consequences. | 机器通过尝试、得到反馈，再慢慢学会怎么做更好。 |
| reinforcement learning | 强化学习 | Learning actions by interacting with a world. | 一边行动一边根据结果学习。 |
| machine-learning method | 机器学习方法 | A way to make a system learn from experience or data. | 让机器通过经验变聪明的一种方法。 |
| agent | 智能体；代理 | The decision-making system that chooses actions. | 负责做决定的机器或程序。 |
| Agent | 智能体；代理 | The system that makes decisions. | 页面定义中的“做决定的系统”。 |
| decision-making system | 决策系统 | A system that selects what to do. | 根据情况选择下一步的系统。 |
| environment | 环境 | The world that the agent interacts with. | 智能体所在并会对它产生反应的世界。 |
| Environment | 环境 | The world in which the agent operates. | 智能体要面对的外部世界。 |
| interaction | 交互 | The agent acts and receives results from the environment. | 智能体做事，环境再给出结果。 |
| action | 动作；行动 | Something the agent chooses to do. | 智能体采取的一个具体动作。 |
| Action | 动作；行动 | What the agent chooses. | 智能体要做什么的选择。 |
| reward | 奖励；回报 | Feedback about the result of an action. | 告诉机器这一步结果好不好的一种分数或信号。 |
| Reward | 奖励；回报 | A feedback signal from the outcome. | 对行为结果的反馈，不一定是钱或真正的奖品。 |
| consequence | 后果；结果 | What happens after an action. | 做了某件事之后发生的结果。 |
| feedback | 反馈 | Information about how an action turned out. | 告诉系统行为效果的信息。 |
| result | 结果 | What follows an attempted action. | 一次尝试之后得到的结果。 |
| policy | 策略；策略函数 | A rule for choosing actions in situations. | 在不同情况下应该怎么行动的规则。 |
| long-term reward | 长期奖励；长期回报 | Reward accumulated over time. | 不只看眼前得分，还看长期总效果。 |
| goal | 目标 | The outcome the learner tries to optimize. | 强化学习想要达到的方向。 |
| learning from rewards | 从奖励中学习 | Improving behavior using reward feedback. | 根据奖励高低调整行为。 |
| learning from consequences | 从后果中学习 | Changing behavior after seeing outcomes. | 看事情结果后改进下一次做法。 |
| choose actions | 选择动作 | Select an action to take. | 从几个可能做法中挑一个。 |
| better long-term reward | 更好的长期回报 | A policy that achieves more useful reward over time. | 眼前不一定最好，但长期结果更好的做法。 |
| state | 状态 | The current situation observed by an agent. | 当前局面或环境情况。 |
| State | 状态 | A snapshot of the current situation. | 某一时刻世界是什么样子。 |
| observes state | 观察状态 | The agent reads the current situation. | 智能体先看看当前局面。 |
| agent observes state | 智能体观察状态 | The agent receives information about the current state. | 智能体获取当前环境信息。 |
| current state | 当前状态 | The situation at this moment. | 现在所处的局面。 |
| current board | 当前棋盘 | The present board configuration in a game. | 游戏此刻棋盘上的摆法。 |
| current context | 当前上下文；当前情境 | The information describing the current situation. | 当前推荐或决策所依据的背景信息。 |
| robot position | 机器人位置 | Where the robot is currently located. | 机器人现在处在什么地方。 |
| environment changes | 环境变化 | The world updates after an action. | 智能体行动后，外部世界发生变化。 |
| receive reward | 获得奖励 | Get feedback after an action. | 做完动作后收到反馈。 |
| update behavior | 更新行为 | Adjust future actions based on feedback. | 根据结果修改以后怎么做。 |
| repeat | 重复 | Run the interaction cycle again. | 不断循环尝试。 |
| interaction loop | 交互循环 | Observe, act, receive feedback, and improve repeatedly. | 看情况、行动、收反馈、调整，再循环。 |
| learning process | 学习过程 | The sequence through which behavior improves. | 行为逐步变好的过程。 |
| attempt | 尝试 | One effort to take an action. | 试着做一次。 |
| move | 移动；走法 | An action in a game or physical task. | 在棋类或机器人任务中的一步动作。 |
| game | 游戏 | An environment in which an agent can learn actions. | 可以通过输赢反馈学习的场景。 |
| game playing | 游戏对弈；游戏操控 | Using learning to choose game moves. | 让机器学会玩游戏或下棋。 |
| game-playing agent | 游戏智能体 | An agent that learns to play a game. | 学习怎么赢游戏的程序。 |
| good decision | 好决策 | A decision that tends to produce a useful result. | 更可能带来好结果的选择。 |
| poor decision | 差决策 | A decision that tends to produce a bad result. | 更可能带来坏结果的选择。 |
| good outcome | 好结果 | A favorable result of an action. | 事情朝有利方向发展的结果。 |
| poor outcome | 差结果 | An unfavorable result of an action. | 事情结果不理想。 |
| over many attempts | 多次尝试之后 | Learning from repeated trials. | 不是试一次，而是反复积累经验。 |
| tend to work better | 往往更有效 | An action is more likely to produce a good result. | 某种做法通常更容易成功。 |
| real-world example | 现实世界实例 | An example of applying RL outside a toy explanation. | 强化学习在真实问题中的用法。 |
| game playing example | 游戏对弈实例 | RL applied to choosing a game move. | 通过棋盘局面决定下一步。 |
| robot learning | 机器人学习 | A robot improves its actions through feedback. | 机器人通过试错学会移动或完成任务。 |
| robot | 机器人 | A physical system that can observe and act. | 能感知并执行动作的机器。 |
| progress toward goal | 朝目标前进 | Reward based on how much an action advances the task. | 离目标更近了就可能得到更好的反馈。 |
| recommendation system | 推荐系统 | A system that selects options for a user. | 给用户挑选内容或选项的系统。 |
| decision system | 决策系统 | A system that chooses among alternatives. | 帮助选择下一步方案的系统。 |
| recommendation / decision system | 推荐／决策系统 | A system that chooses an option based on context and outcomes. | 根据当前情况挑一个选项的系统。 |
| measured outcome | 可测量结果 | An outcome used as feedback or reward. | 可以被记录、比较或打分的结果。 |
| choose an option | 选择一个选项 | Pick one available alternative. | 从多个选项里挑一个。 |
| current context | 当前上下文；当前情境 | The situation used to make a recommendation or decision. | 做推荐或决策时眼前的背景信息。 |
| recommendation | 推荐 | Suggesting an option to a user. | 给用户建议看什么、买什么或做什么。 |
| not all recommendation systems are reinforcement learning | 并非所有推荐系统都是强化学习 | A recommendation system may use other methods. | 有推荐功能不代表它一定用了强化学习。 |
| supervised learning | 监督学习 | Learning from examples that include supplied correct answers. | 训练数据直接告诉机器标准答案。 |
| Supervised Learning | 监督学习 | A learning setup with a target label for each example. | 每道题都有已知答案，机器照着学。 |
| correct answer | 正确答案 | The supplied target answer for a supervised example. | 数据中明确给出的标准答案。 |
| supplied correct answer | 提供的正确答案 | A target answer given during training. | 训练时直接提供给模型的答案。 |
| example | 样本；例子 | One training case or situation. | 用来学习的一条数据或一个情境。 |
| target label | 目标标签 | The expected label or answer for an example. | 每条样本对应的标准分类或结果。 |
| label | 标签 | A known category or target attached to data. | 给数据贴上的已知答案标记。 |
| unsupervised learning | 无监督学习 | Learning structure from data without supplied labels. | 没有标准答案，自己找数据里的规律。 |
| Unsupervised Learning | 无监督学习 | Finding patterns in unlabeled data. | 从没有标签的数据中发现结构。 |
| unlabeled data | 无标签数据 | Data that has no supplied correct answer. | 数据没有附带人工标准答案。 |
| structure | 结构；规律 | A pattern or organization found in data. | 数据内部隐藏的分组或规律。 |
| reward signal | 奖励信号 | A signal indicating how an action turned out. | 用一个信号告诉系统这一步表现如何。 |
| feedback signal | 反馈信号 | A signal about the result, not necessarily a target answer. | 对结果的评价信号，不是题目标准答案。 |
| reward ≠ correct answer | 奖励不等于正确答案 | A reward evaluates an outcome; it is not necessarily a target label. | 奖励只表示结果好不好，不一定告诉你唯一答案。 |
| reinforcement learning setup | 强化学习设置；强化学习框架 | The combination of agent, environment, actions, and rewards. | 智能体、环境、动作、奖励组成的完整场景。 |
| agent + environment | 智能体＋环境 | The learner and the world it interacts with. | 做事的机器和它所在的世界。 |
| actions + rewards | 动作＋奖励 | Choices and feedback in the learning cycle. | 机器怎么做，以及做完得到什么反馈。 |
| machine learning | 机器学习 | A broader field that includes supervised, unsupervised, and reinforcement learning. | 让机器从数据或经验中学习的大类。 |
| Machine Learning | 机器学习 | The broader category containing several learning approaches. | 强化学习所属的上位概念。 |
| learning approach | 学习方式 | A general way for a system to learn. | 机器学习信息的不同路线。 |
| related concept | 相关概念 | A concept connected to reinforcement learning. | 和强化学习有关系、值得一起理解的词。 |
| AI agent | AI 智能体 | An AI system that can make decisions and take actions. | 能根据情况自主做事的 AI 系统。 |
| agent loop | 智能体循环 | A repeated cycle in which an agent observes, acts, and updates. | 智能体不断感知、行动、得到结果的循环。 |
| Agent Loop | 智能体循环 | The recurring observe-act-feedback pattern. | “看一看、做一做、根据结果调整”的循环。 |
| long-term optimization | 长期优化 | Improving total future reward rather than only immediate feedback. | 为了未来整体效果而优化。 |
| immediate reward | 即时奖励 | Feedback received soon after an action. | 做完一步很快收到的反馈。 |
| delayed consequence | 延迟后果 | An outcome that appears later. | 现在的动作可能过一会儿才看出好坏。 |
| trial and error | 试错 | Learning by trying actions and observing outcomes. | 通过不断试验和犯错学会更好的办法。 |
| experience | 经验 | Past interactions used to improve future decisions. | 之前尝试留下的可学习信息。 |
| behavior | 行为 | The pattern of actions selected by an agent. | 智能体通常怎么行动。 |
| behavior update | 行为更新 | A change to action choices after feedback. | 根据奖励调整行动方式。 |
| decision | 决策 | A choice about which action to take. | 在当前情况下决定做什么。 |
| choice | 选择 | Selecting one action or option. | 从可能的动作中挑一个。 |
| action selection | 动作选择 | The process of choosing an action. | 决定下一步做哪个动作。 |
| state-action pair | 状态-动作对 | A state together with an action taken in it. | 在某个局面下采取的某个动作。 |
| trajectory | 轨迹；经历序列 | A sequence of states, actions, and outcomes. | 一连串“看到什么、做什么、结果怎样”的记录。 |
| episode | 回合；幕 | One complete run of interaction from start to end. | 从开始到结束的一次完整尝试。 |
| return | 回报总和 | The accumulated reward from a run. | 一次经历中累积得到的总奖励。 |
| score | 得分 | A numeric measure of an outcome in a game or task. | 用数字表示表现好坏。 |
| win / lose / score | 胜／负／得分 | Possible game outcomes used as feedback. | 游戏里赢、输或得分都可以作为反馈。 |
| measured progress | 可测量的进展 | Quantified movement toward a goal. | 用数字衡量离目标近了多少。 |
| optimization objective | 优化目标 | What the learning process tries to improve. | 训练时希望最大化或最小化的东西。 |
| reward design | 奖励设计 | Choosing how outcomes are converted into feedback. | 设计什么结果应该给多少奖励。 |
| deployment use case | 部署用例 | A practical context where a trained policy is used. | 训练好的系统真正投入使用的场景。 |
| policy behavior | 策略行为 | The actions produced by a policy. | 策略在实际情况下表现出来的动作。 |
| agent-environment interaction | 智能体-环境交互 | The two-way process between the learner and its world. | 智能体行动、环境回应的来回过程。 |
| feedback-driven learning | 反馈驱动学习 | Learning guided by outcome feedback. | 主要靠结果反馈来改进。 |
| consequence-based learning | 基于后果的学习 | Learning by relating actions to later outcomes. | 通过行动后果判断哪些做法更好。 |
| action outcome | 动作结果 | What happens after an action is taken. | 某个动作带来的实际结果。 |
| next action | 下一步动作 | The action chosen after observing the updated situation. | 环境变化后接着要做的事。 |
| current situation | 当前情况 | The information available before choosing an action. | 做决定之前眼前的局面。 |
| learning by playing | 通过玩来学习 | Learning a game through repeated play. | 像人打游戏一样边玩边学。 |
| game move | 游戏走法；游戏动作 | A selected action in a game. | 游戏中的一步棋或一次操作。 |
| physical action | 物理动作 | An action performed by a robot or other physical system. | 机器人在现实世界里真的移动或操作。 |
| option | 选项 | One possible choice available to the agent. | 可以选择的一个方案。 |
| outcome feedback | 结果反馈 | Information evaluating an outcome. | 对结果好坏的反馈。 |
| learning objective | 学习目标 | The behavior or reward outcome the learner seeks. | 希望机器最终学会什么。 |
| policy improvement | 策略改进 | Making the action-selection rule produce better results. | 让“遇到这种情况怎么做”的规则越来越好。 |
| RL | 强化学习缩写 | Short form for reinforcement learning. | Reinforcement Learning 的常见缩写。 |
| AI | 人工智能 | A broad field including systems that perceive, decide, or act. | 让机器表现出智能能力的大领域。 |
| ML | 机器学习缩写 | Short form for machine learning. | Machine Learning 的常见缩写。 |
| environment response | 环境响应 | How the environment reacts to an agent action. | 外部世界对机器动作的回应。 |
| action consequence | 动作后果 | The result caused by an action. | 一个动作之后产生的影响。 |
| repeated interaction | 重复交互 | Interacting with the environment many times. | 和环境反复来回沟通。 |
| future behavior | 未来行为 | Actions the agent will choose later. | 系统以后会怎么做。 |
| reward accumulation | 奖励累积 | Adding feedback across multiple steps. | 把多步奖励加起来看整体效果。 |
| feedback loop | 反馈回路 | A cycle where outputs affect future behavior. | 结果会反过来影响下一次行为的循环。 |

## Potential Missing Concepts

以下词在当前页面没有展开定义，但它们是后续完整强化学习词汇表通常需要补齐的候选概念；保留在“潜在缺失”区，不把它们误当成页面已经讲过的内容：

- Markov Decision Process (MDP)；马尔可夫决策过程
- state transition；状态转移
- transition dynamics；转移动力学
- initial state；初始状态
- terminal state；终止状态
- action space；动作空间
- state space；状态空间
- observation space；观测空间
- partial observability；部分可观测性
- reward function；奖励函数
- value function；价值函数
- state-value function；状态价值函数
- action-value function；动作价值函数
- Q-value；Q 值
- Q-function；Q 函数
- optimal value；最优价值
- optimal policy；最优策略
- discount factor / discount rate；折扣因子／折扣率
- discounted return；折扣回报
- exploration；探索
- exploitation；利用
- exploration-exploitation trade-off；探索与利用权衡
- epsilon-greedy；ε-贪心
- stochastic policy；随机策略
- deterministic policy；确定性策略
- on-policy learning；同策略学习
- off-policy learning；异策略学习
- model-free reinforcement learning；无模型强化学习
- model-based reinforcement learning；基于模型的强化学习
- environment model；环境模型
- planning；规划
- Monte Carlo method；蒙特卡洛方法
- temporal-difference learning (TD learning)；时序差分学习
- TD error；时序差分误差
- Bellman equation；贝尔曼方程
- Bellman optimality equation；贝尔曼最优方程
- dynamic programming；动态规划
- Q-learning；Q 学习
- SARSA；SARSA 算法
- deep Q-network (DQN)；深度 Q 网络
- replay buffer / experience replay；经验回放缓冲区／经验回放
- target network；目标网络
- policy gradient；策略梯度
- actor-critic；演员-评论家
- actor；演员网络
- critic；评论家网络
- advantage function；优势函数
- advantage estimation；优势估计
- proximal policy optimization (PPO)；近端策略优化
- trust region policy optimization (TRPO)；信赖域策略优化
- deterministic policy gradient；确定性策略梯度
- multi-armed bandit；多臂老虎机
- contextual bandit；上下文老虎机
- reward shaping；奖励塑形
- sparse reward；稀疏奖励
- dense reward；密集奖励
- reward hacking；奖励投机／奖励黑客
- credit assignment；信用分配
- temporal credit assignment；时间信用分配
- delayed reward；延迟奖励
- curriculum learning；课程学习
- imitation learning；模仿学习
- inverse reinforcement learning；逆强化学习
- preference learning；偏好学习
- human feedback；人类反馈
- RLHF；基于人类反馈的强化学习
- RLAIF；基于 AI 反馈的强化学习
- preference model；偏好模型
- reward model；奖励模型
- policy model；策略模型
- safe reinforcement learning；安全强化学习
- constrained reinforcement learning；约束强化学习
- offline reinforcement learning；离线强化学习
- online reinforcement learning；在线强化学习
- batch reinforcement learning；批量强化学习
- multi-agent reinforcement learning (MARL)；多智能体强化学习
- cooperative multi-agent learning；协作式多智能体学习
- competitive multi-agent learning；竞争式多智能体学习
- self-play；自博弈
- simulator；模拟器
- simulation-to-real transfer；从仿真到现实迁移
- transfer learning；迁移学习
- generalization；泛化
- reward normalization；奖励归一化
- observation normalization；观测归一化
- training instability；训练不稳定
- sample efficiency；样本效率
- policy evaluation；策略评估
- policy iteration；策略迭代
- value iteration；价值迭代
- convergence；收敛
- regret；遗憾值
- cumulative reward；累计奖励
- average reward；平均奖励
- success rate；成功率
- episode length；回合长度
- baseline；基线
- random policy；随机策略
- greedy policy；贪心策略
- agent safety；智能体安全
- action constraints；动作约束
- reward monitoring；奖励监控
- evaluation environment；评估环境
- training environment；训练环境
- inference-time policy；推理时策略
- deployment monitoring；部署监控

## Aliases / Synonyms

- Reinforcement Learning / RL / 强化学习
- agent / learner / decision-making system / 智能体／学习者／决策系统
- environment / world / task world / 环境／世界／任务世界
- action / move / choice / decision / 动作／走法／选择／决策
- reward / return / payoff / feedback signal / 奖励／回报／收益／反馈信号
- consequence / outcome / result / effect / 后果／结果／影响
- state / situation / current situation / current context / 状态／局面／当前情况／当前上下文
- policy / behavior policy / action-selection rule / 策略／行为策略／动作选择规则
- game playing / game playing agent / game-playing task / 游戏对弈／游戏智能体／游戏任务
- robot learning / robotic reinforcement learning / 机器人学习／机器人强化学习
- recommendation system / recommender system / 推荐系统
- decision system / decision-making system / 决策系统／决策制定系统
- supervised learning / supervised ML / 监督学习／监督式机器学习
- unsupervised learning / unsupervised ML / 无监督学习／无监督式机器学习
- correct answer / target answer / target label / ground-truth label / 正确答案／目标答案／目标标签／真实标签
- reward signal / feedback signal / outcome signal / 奖励信号／反馈信号／结果信号
- long-term reward / cumulative reward / return / 长期奖励／累计奖励／回报
- interaction loop / agent loop / feedback loop / 交互循环／智能体循环／反馈回路
- trial and error / learning by trying / 试错／通过尝试学习
- RL setup / reinforcement learning setup / 强化学习设置／强化学习框架

## Do Not Confuse Candidates

- Reinforcement Learning vs Supervised Learning：强化学习通常从交互结果和奖励学习；监督学习对每个样本提供正确答案或目标标签。
- Reinforcement Learning vs Unsupervised Learning：无监督学习主要从无标签数据中找结构；强化学习主要学习在环境中采取哪些动作。
- Reward vs Correct Answer：奖励是反馈信号，可能只是一个分数或好坏指示；正确答案是监督样本里的目标答案。
- Reward vs Return：reward 通常指某一步或某次结果的反馈；return 通常指一段经历中累积的奖励总和。
- Reward vs Score：score 可以是游戏得分或评价数值；reward 是训练循环用于反馈和更新行为的信号，二者在具体系统中可能相同，也可能不同。
- Reward vs Outcome：outcome 是发生了什么；reward 是系统如何把结果转成反馈信号。
- Agent vs Environment：agent 是做决定的一方；environment 是被交互的外部世界。
- Agent vs AI Agent：页面中的 agent 是强化学习中的角色；AI agent 是更宽泛的能感知、决策或行动的 AI 系统，未必使用强化学习。
- Action vs Policy：action 是一次具体动作；policy 是在不同状态下选择动作的规则或函数。
- State vs Environment：state 是环境在某一时刻的状态描述；environment 是包含变化规则和反馈的整个世界。
- State vs Observation：state 可理解为环境真实情况；observation 是智能体实际获得的观测，复杂任务中两者可能不同。
- Consequence vs Reward：consequence 是动作造成的后果；reward 是对该后果的反馈编码。
- Recommendation System vs Reinforcement Learning：推荐系统是应用类别，不代表底层一定是强化学习；页面明确提醒并非所有推荐系统都是 RL。
- Long-term Reward vs Immediate Reward：长期奖励关注多步累积效果；即时奖励只关注当前或很快得到的反馈。
- Machine Learning vs Reinforcement Learning：机器学习是更大的领域；强化学习是其中一种学习范式。
- Learning from Interaction vs Learning from Labeled Examples：交互学习依靠行动和反馈；有标签学习依靠预先给出的答案。
- Policy vs Behavior：policy 是产生行为的规则；behavior 是规则实际表现出来的动作模式。
- Game Playing vs Game Engine：game playing 是任务或应用；game engine 是运行游戏世界的软件系统，两者不是同一概念。
- Robot Learning vs Robot Control：机器人学习是通过经验改进行为；机器人控制可以只使用预先设计的控制规则，未必学习。
- Feedback Signal vs Label：反馈信号评价行为结果；标签是数据样本的目标标记。
- Exploration vs Random Mistakes：探索是为了获得新信息而尝试动作；随机错误只是失败，不一定具有探索目的。
- Agent Loop vs Ordinary Program Loop：智能体循环通常根据环境反馈更新行为；普通程序循环可能只是重复执行固定代码。
- Reward Design vs Policy Design：奖励设计决定什么被认为是好结果；策略设计决定如何根据状态选择动作。

## Notes

- 本 raw 文件按页面正文及直接相关上下文做“最大候选收集”，不去重、不删减；重复术语保留，以便后续清洗阶段判断是否合并。
- 页面核心叙事是：agent 与 environment 交互，观察 state，选择 action，环境变化，收到 reward，更新 behavior，然后重复。
- 页面最明确的目标表述是：学习一个能产生更好长期奖励的 policy。
- 页面用“学习玩游戏”作类比：尝试动作、得到结果、好决策带来奖励、坏决策带来较差结果，经过多次尝试学到更有效的动作。
- 页面实例包括 Game Playing、Robot Learning、Recommendation / Decision Systems，并分别使用 current board、robot position、current context 作为 state 示例。
- 页面给出的奖励示例包括 win / lose / score、progress toward goal、measured outcome。
- 页面明确区分强化学习、监督学习、无监督学习，也明确区分 reward 与 correct answer。
- 页面链接的直接相关主题包括 Machine Learning、AI Agent、Agent Loop、Supervised Learning；这些已纳入候选或关系上下文。
- 页面没有展开算法名称、数学公式、MDP、Q-learning、policy gradient、RLHF 等高级内容；它们已列入 Potential Missing Concepts，待后续模块或资料核验。
- 页面 video 区块只有“No video asset available yet”和“A video explanation will be added when a real source is available.”，没有可新增的视频术语或来源事实。
- 该文件仅为 glossary-work/raw 的原始收集稿，不应直接视为最终去重、排序或事实核验后的术语表。
