# Topic

Machine Learning

Module: 01 · AI Foundations

Topic: Machine Learning

Source File: `machine-learning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Machine Learning | 机器学习 | A way for computers to learn patterns from examples. | 让电脑从很多例子中自己找规律，而不是每条规则都由人写好。 |
| ML | 机器学习缩写 | Short for Machine Learning. | Machine Learning 的英文缩写。 |
| Artificial Intelligence | 人工智能 | The broad field of making machines perform tasks that appear intelligent. | 人工智能是更大的总领域，机器学习只是其中一种实现方式。 |
| AI | 人工智能缩写 | Short for Artificial Intelligence. | Artificial Intelligence 的英文缩写。 |
| Deep Learning | 深度学习 | A Machine Learning approach using neural networks with many layers. | 深度学习是机器学习的一种，通常使用很多层的神经网络。 |
| DL | 深度学习缩写 | Short for Deep Learning. | Deep Learning 的英文缩写。 |
| Foundation Model | 基础模型 | A broadly trained model reusable across many tasks. | 先广泛学习、以后可以改造成很多用途的模型。 |
| Supervised Learning | 监督学习 | Learning from examples that include correct answers. | 训练例子里带着标准答案，模型照着答案学习。 |
| Unsupervised Learning | 无监督学习 | Finding patterns in data without predefined labels. | 没有标准答案时，模型自己寻找分组和结构。 |
| Reinforcement Learning | 强化学习 | Learning actions through interaction, feedback, and rewards. | 模型通过做动作、得到奖励或惩罚来学会怎么做。 |
| Learning approach | 学习方式 | A general way a system learns. | 描述系统学习路径的类别，例如监督、无监督、强化学习。 |
| Rule-based system | 基于规则的系统 | A system that follows explicitly written rules. | 人把规则写出来，系统按规则执行。 |
| Fixed-rule programming | 固定规则编程 | Programming where rules are explicitly written by a developer. | 开发者直接写出“如果……那么……”的固定规则。 |
| Learned system | 学习型系统 | A system whose behavior is learned from data. | 系统的行为主要通过数据训练出来，而不是全靠手写规则。 |
| Model | 模型 | A learned structure that turns inputs into useful outputs. | 模型像一个学会规律的“计算器”，接收输入后给出结果。 |
| Trained model | 训练好的模型 | A model after it has learned from training examples. | 已经看过训练资料并留下规律的模型。 |
| Learned model | 学到规律的模型 | Another description of a model that has learned patterns. | 强调模型已经从例子里学到了可复用的模式。 |
| Algorithm | 算法 | A procedure for solving a problem or learning from data. | 解决问题或从数据学习的一套步骤。 |
| Method | 方法 | A particular technique used to learn or make predictions. | 完成学习或预测任务的具体办法。 |
| Pattern | 模式 / 规律 | A repeatable relationship found in examples. | 许多例子中反复出现的关系或规律。 |
| Representation | 表示 / 表征 | A form in which data is encoded for a model. | 把现实数据转换成模型更容易处理的形式。 |
| Learned representation | 学到的表征 | A useful representation discovered during training. | 模型训练过程中自己学会的特征表达。 |
| Data | 数据 | Information used by or produced for a system. | 提供给系统的各种信息，例如邮件、销量、日历记录。 |
| Training data | 训练数据 | Examples used to teach a model. | 用来教模型的样本集合。 |
| Dataset | 数据集 | An organized collection of data examples. | 按一定结构收集起来的一批数据。 |
| Example | 示例 / 例子 | One case shown to the learning system. | 给模型看的一个具体案例。 |
| Sample | 样本 | One unit of data in a dataset. | 数据集中的一条记录或一个案例。 |
| Instance | 实例 | One individual data case. | 一个独立的数据对象，和 sample 类似。 |
| Record | 记录 | One stored row or item of information. | 数据表里的一行，或系统保存的一条信息。 |
| Input | 输入 | Data supplied to a model. | 送进模型、让模型处理的内容。 |
| New input | 新输入 | Data the model receives after training. | 模型训练后遇到的新案例。 |
| Expected outcome | 预期结果 | The result expected for an input during practice. | 训练时告诉模型“这个输入应该得到什么结果”。 |
| Target | 目标值 / 目标答案 | The answer a model is trained to predict. | 模型要学着预测的标准目标。 |
| Label | 标签 | A named answer attached to an example. | 给样本贴上的答案类别，例如“垃圾邮件”。 |
| Labeled data | 有标签数据 | Data paired with known answers. | 每条数据旁边都有已知答案的数据。 |
| Unlabeled data | 无标签数据 | Data without predefined answers. | 只有原始数据，没有提前写好的答案。 |
| Feature | 特征 | An input property useful for learning. | 数据中可能帮助判断结果的属性，例如价格或日期。 |
| Feature vector | 特征向量 | A numeric representation of multiple features. | 把多个特征排成一组数字给模型使用。 |
| Ground truth | 真实值 / 标准答案 | The trusted answer used as a reference. | 用来检查模型对不对的可信标准答案。 |
| Model parameters | 模型参数 | Internal values learned from training data. | 模型通过训练自动调整、用来保存规律的内部数字。 |
| Parameters | 参数 | Learned internal values that affect model behavior. | 决定模型行为的一组内部数值。 |
| Weights | 权重 | Numeric values that control the importance of signals. | 模型给不同信息分配的“重要程度”。 |
| Internal values | 内部数值 | Values changed while a model learns. | 训练中不断调整的模型内部数字。 |
| Hyperparameter | 超参数 | A setting chosen for the learning process rather than learned directly. | 训练前由人设置的学习选项，例如学习速度。 |
| Settings | 设置 / 参数设置 | Choices that control how learning happens. | 控制训练过程如何进行的选项。 |
| Learning rate | 学习率 | How large each learning update is. | 每次调整模型时迈多大一步。 |
| Loss function | 损失函数 | A calculation of how wrong a prediction is. | 用一个数字衡量预测错得有多严重。 |
| Error | 误差 | The difference between a prediction and the expected result. | 模型结果和标准答案之间的差距。 |
| Objective function | 目标函数 | A quantity the training process tries to optimize. | 训练时希望变好或变小的评价数值。 |
| Optimization | 优化 | Adjusting a model to improve its objective. | 不断调整模型，让错误更少、结果更好。 |
| Gradient descent | 梯度下降 | An optimization method that reduces loss step by step. | 沿着让错误下降的方向一点点调整参数。 |
| Epoch | 训练轮次 | One pass through the training data. | 把整份训练数据完整看一遍。 |
| Batch | 批次 | A group of examples processed together. | 一次拿来计算的一小批样本。 |
| Mini-batch | 小批次 | A small batch used for one training update. | 训练时分批处理数据的一个小组。 |
| Training | 训练 | Turning examples into a learned model. | 让模型反复看例子并调整内部数值的过程。 |
| Learning | 学习 | The process of discovering useful patterns from data. | 从数据中找出可以复用规律的过程。 |
| Training process | 训练过程 | The sequence that converts examples into a model. | 从准备例子到形成模型的一整套流程。 |
| Training pipeline | 训练流水线 | A repeatable sequence for preparing data and training a model. | 把数据准备、训练、检查等步骤串起来的流程。 |
| Inference | 推理 / 推断 | Applying a learned model to new data. | 模型学会后，用它处理新数据并给出结果。 |
| Prediction | 预测 | A result returned for a new input. | 模型对新案例给出的判断或数值。 |
| Output | 输出 | The result produced by a model. | 模型处理输入后返回的结果。 |
| Result | 结果 | The response produced by a system. | 系统最后给用户或下游程序的答案。 |
| Classification | 分类 | Predicting a category or label. | 判断输入属于哪个类别，例如垃圾邮件或正常邮件。 |
| Class | 类别 | One possible category in a classification task. | 分类问题中的一个选项或类型。 |
| Regression | 回归 | Predicting a numerical value. | 预测一个数值，例如价格或销量。 |
| Forecast | 预测 / 预报 | A prediction about a future value or event. | 对未来会发生什么、数值会是多少的估计。 |
| Ranking | 排序 | Ordering possible items by relevance or score. | 按相关性或可能性给候选项排顺序。 |
| Recommendation | 推荐 | Suggesting items likely to be useful or interesting. | 根据用户情况挑出可能喜欢或需要的内容。 |
| Recommendation list | 推荐列表 | A short ordered list of suggested items. | 系统推荐给用户的一小串候选内容。 |
| Recommender system | 推荐系统 | A system that ranks or suggests items for a user. | 根据用户行为推荐商品、视频或文章的系统。 |
| Score | 分数 / 得分 | A numeric value used to compare or rank outputs. | 帮助比较结果好坏或优先级的数字。 |
| Probability | 概率 | A number expressing how likely an outcome is. | 表示某种结果可能发生多大的数值。 |
| Spam filter | 垃圾邮件过滤器 | A system that identifies unwanted email. | 自动判断邮件是不是垃圾邮件的功能。 |
| Spam classifier | 垃圾邮件分类器 | A classifier for spam versus non-spam messages. | 专门把邮件分成垃圾和非垃圾的分类模型。 |
| Demand forecast | 需求预测 | An estimate of future demand. | 预测未来需要多少商品或服务。 |
| Demand forecasting | 需求预测过程 | Predicting future demand from historical data. | 根据过去销量等资料估计未来需求。 |
| User history | 用户历史记录 | Past actions or behavior from a user. | 用户过去看过、买过或点击过什么。 |
| Similar behavior | 相似行为 | Behavior patterns shared by users or examples. | 不同用户或样本表现出的相近行为模式。 |
| Calendar data | 日历数据 | Date and time information used as input. | 周几、月份、节假日等日期相关资料。 |
| Sales data | 销售数据 | Records of past sales. | 过去卖了多少、什么时候卖的数据。 |
| Future stock needs | 未来库存需求 | Expected inventory needed later. | 未来可能要准备多少库存。 |
| Generalization | 泛化 | Performing well on new data beyond training examples. | 不只是背会训练题，而是遇到新题也能做好。 |
| Overfitting | 过拟合 | Learning training examples too specifically and failing on new data. | 把练习题背得太死，换新题就不会了。 |
| Underfitting | 欠拟合 | Failing to learn enough useful structure from the data. | 连训练资料里的基本规律都没学好。 |
| Held-out data | 留出数据 | Data kept separate for checking a model. | 训练时先不让模型看的数据，用来检验效果。 |
| Train-validation-test split | 训练集-验证集-测试集划分 | Dividing data for learning, tuning, and final checking. | 把数据分成学习、调参和最后验收几部分。 |
| Training set | 训练集 | The portion of data used to fit a model. | 真正拿来教模型的那部分数据。 |
| Validation set | 验证集 | Data used to choose settings and compare versions. | 用来调设置、比较模型方案的数据。 |
| Test set | 测试集 | Data used for a final unbiased check. | 最后验收模型、尽量不参与训练的数据。 |
| Data leakage | 数据泄漏 | Training receives information it should not have. | 不该提前看到的答案偷偷进入了训练。 |
| Data distribution | 数据分布 | How values and patterns are spread in data. | 数据中各类情况出现的比例和规律。 |
| Distribution shift | 分布变化 | The real-world data differs from training data. | 上线后遇到的数据和训练时不一样了。 |
| Data drift | 数据漂移 | Data characteristics change over time. | 数据的规律随着时间慢慢变了。 |
| Concept drift | 概念漂移 | The relationship between inputs and outcomes changes. | 同样的输入和结果之间的关系变了。 |
| Evaluation | 评估 | Testing whether predictions meet the intended need. | 检查模型结果是否有用、可靠、适合任务。 |
| Metric | 指标 | A measurable quantity used to judge performance. | 用来量化模型表现的数字。 |
| Accuracy | 准确率 | The fraction of predictions that are correct. | 所有判断里答对的比例。 |
| Precision | 精确率 | Among predicted positives, the share that is correct. | 模型说“是”的那些里，真正是的比例。 |
| Recall | 召回率 | Among actual positives, the share found by the model. | 所有真正的目标里，模型找出来的比例。 |
| F1 score | F1 分数 | A combined measure of precision and recall. | 综合考虑精确率和召回率的分数。 |
| Mean squared error | 均方误差 | Average squared difference between predictions and targets. | 把预测差距平方后取平均来衡量错误。 |
| MAE | 平均绝对误差 | Mean absolute difference between predictions and targets. | 预测值和真实值差多少，取绝对值再平均。 |
| RMSE | 均方根误差 | The square root of mean squared error. | 对均方误差开根号后的误差指标。 |
| Benchmark | 基准测试 | A standard comparison used to measure models. | 用统一题目或数据比较不同模型的测试。 |
| Test case | 测试案例 | A chosen input and expected behavior for checking a system. | 用来检查系统表现的一条具体案例。 |
| Error analysis | 错误分析 | Inspecting where and why predictions fail. | 仔细看模型错在什么地方、为什么会错。 |
| Monitoring | 监控 | Watching a deployed model and its data over time. | 上线后持续观察模型和数据有没有异常。 |
| Deployment | 部署 | Making a trained model available for use. | 把训练好的模型放到真实系统里使用。 |
| Model serving | 模型服务 | Running a model so applications can request predictions. | 让应用可以调用模型并得到预测结果。 |
| Prediction service | 预测服务 | A service that accepts inputs and returns predictions. | 接收输入并返回模型结果的线上服务。 |
| Latency | 延迟 | Time between a request and its response. | 用户发出请求后等多久才能拿到结果。 |
| Throughput | 吞吐量 | How many requests or examples a system handles per unit time. | 单位时间内系统能处理多少请求或数据。 |
| Reliability | 可靠性 | The ability to perform consistently as expected. | 模型在不同时间和情况下都能稳定工作。 |
| Robustness | 鲁棒性 / 稳健性 | Ability to remain useful under variation or noise. | 数据有变化或有干扰时仍不容易失效。 |
| Bias | 偏差 / 偏见 | Systematic error or unequal behavior caused by data or design. | 数据或设计造成的系统性错误，也可能导致不公平。 |
| Fairness | 公平性 | Whether performance and treatment are acceptably fair across groups. | 不同人群是否被合理、平等地对待。 |
| Interpretability | 可解释性 | How understandable a model’s behavior is. | 人能不能看懂模型为什么这样判断。 |
| Privacy | 隐私 | Protection of information about people or organizations. | 防止训练和使用过程泄露个人或组织信息。 |
| Human review | 人工复核 | A person checks or approves model outputs. | 重要结果交给人再看一遍或确认。 |
| Safety | 安全性 | Avoiding harmful or unacceptable behavior. | 防止模型输出或行动造成伤害。 |
| Neural network | 神经网络 | A model made of connected layers that transform signals. | 由多层相互连接的计算单元组成的模型。 |
| Multi-layer neural network | 多层神经网络 | A neural network with multiple processing layers. | 有很多层、逐层提取规律的神经网络。 |
| Decision tree | 决策树 | A model that makes decisions through branching conditions. | 像流程图一样按条件一层层分叉判断。 |
| Random forest | 随机森林 | An ensemble of many decision trees. | 同时用很多棵决策树再综合它们的判断。 |
| Linear model | 线性模型 | A model that combines inputs using a linear relationship. | 按输入的加权组合来计算结果的模型。 |
| Linear regression | 线性回归 | A linear model for predicting numeric values. | 用线性关系预测价格、销量等数值。 |
| Logistic regression | 逻辑回归 | A model often used to predict class probabilities. | 常用来判断类别，并给出属于某类的概率。 |
| Clustering | 聚类 | Grouping similar examples without predefined labels. | 把相似数据自动分成几组。 |
| K-means | K 均值聚类 | A clustering algorithm that forms a chosen number of groups. | 预先指定组数，再把相近样本分到这些组。 |
| Dimensionality reduction | 降维 | Representing data with fewer dimensions while retaining useful structure. | 用更少的数字表示数据，同时尽量保留重要规律。 |
| Nearest-neighbor method | 近邻方法 | Predicting from similar examples nearby in feature space. | 看和当前样本最相似的几个例子来判断。 |
| Support vector machine | 支持向量机 | A model that separates classes using a boundary. | 找一条能把不同类别分开的边界。 |
| Ensemble model | 集成模型 | A model that combines multiple models. | 把多个模型的意见合在一起，通常更稳。 |
| Model type | 模型类型 | A category of model architecture or method. | 模型按照结构或算法划分的类别。 |
| Model family | 模型家族 | A group of related model designs. | 结构或用途相近的一组模型。 |
| Architecture | 架构 | The structural design of a model. | 模型内部各部分如何组织的设计。 |
| Feature engineering | 特征工程 | Designing useful input features from raw data. | 把原始资料加工成更适合模型学习的特征。 |
| Data preprocessing | 数据预处理 | Cleaning and transforming data before learning. | 训练前清洗、转换和整理数据。 |
| Normalization | 归一化 | Rescaling values to a comparable range. | 把不同尺度的数值调整到相近范围。 |
| Imputation | 缺失值填补 | Filling missing data with suitable values. | 给缺失的数据补上合理的值。 |
| Labeling | 标注 | Assigning labels or target answers to examples. | 给数据加上类别或标准答案。 |
| Data quality | 数据质量 | How accurate, complete, consistent, and useful data is. | 数据是否准确、完整、一致、适合使用。 |
| Data curation | 数据整理 | Selecting and organizing useful training data. | 挑选、清理和组织适合训练的数据。 |
| Feedback | 反馈 | Information about how a result performed. | 告诉系统结果好不好、错在哪里的信息。 |
| Reward | 奖励 | A feedback signal for an action in reinforcement learning. | 强化学习里对动作结果好坏的反馈信号。 |
| Agent | 智能体 | A decision-making system in reinforcement learning. | 在环境里观察并做决定的系统。 |
| Environment | 环境 | The world or setting an agent interacts with. | 智能体进行动作并得到结果的外部世界。 |
| Action | 动作 | A choice made by an agent. | 智能体选择执行的行为。 |
| State | 状态 | The current situation observed by an agent. | 智能体当前所处的情况。 |
| Policy | 策略 | A rule for choosing actions in reinforcement learning. | 根据当前情况决定下一步怎么做的策略。 |
| Long-term reward | 长期奖励 | Reward accumulated over future outcomes. | 不只看眼前得分，还看未来总收益。 |
| Generative AI | 生成式人工智能 | AI aimed at creating new content. | 目标是生成文字、图片、音频等新内容的 AI。 |
| Language model | 语言模型 | A model that learns patterns in language. | 学习文字规律并处理或生成语言的模型。 |
| Vision model | 视觉模型 | A model that learns patterns in images or video. | 学习图片或视频中视觉规律的模型。 |
| Audio model | 音频模型 | A model that learns patterns in sound. | 学习声音或语音规律的模型。 |
| Model adaptation | 模型适配 | Adjusting a general model for a particular task. | 把通用模型调整到某个具体用途。 |
| Fine-tuning | 微调 | Additional training for narrower behavior. | 在已有模型基础上继续训练，让它更适合某个任务。 |
| Prompting | 提示 | Giving instructions or context to a model. | 用指令和上下文引导模型完成任务。 |
| Retrieval | 检索 | Finding relevant information for a model or task. | 从资料库里找出和当前问题相关的信息。 |
| Tool use | 工具使用 | Letting a model call external capabilities. | 让模型调用搜索、计算或其他外部工具。 |
| Database | 数据库 | Explicit records stored for lookup. | 按结构保存原始记录、可以直接查询的地方。 |
| Model parameters versus database records | 模型参数与数据库记录 | Learned values are not the same as explicit stored records. | 模型里的参数不是数据库里一条条可直接查找的原始记录。 |
| Application | 应用 | A concrete use of a model in a product or workflow. | 把模型放进真实产品或工作流程中的用途。 |
| Product | 产品 | A user-facing system built from models and other components. | 面向用户的完整系统，不等于单独一个模型。 |
| Workflow | 工作流程 | A sequence of steps using data, models, and people. | 从输入到结果的一连串工作步骤。 |
| Model card | 模型卡片 | Documentation describing a model’s uses and limits. | 说明模型用途、能力和限制的资料。 |
| Reproducibility | 可复现性 | Ability to obtain consistent results from the same setup. | 别人按同样条件能重现相近结果。 |
| Explainability | 可说明性 | The ability to communicate reasons for model behavior. | 能否用人能理解的方式说明模型为何如此输出。 |
| Calibration | 校准 | Agreement between predicted confidence and actual frequency. | 模型说“八成确定”时，长期看是否真的约八成正确。 |
| Threshold | 阈值 | A cutoff used to turn a score into a decision. | 分数超过某条线就判为某类或采取动作。 |
| Decision boundary | 决策边界 | The boundary separating model decisions or classes. | 模型把不同类别分开的界线。 |
| False positive | 假阳性 / 误报 | A negative case incorrectly predicted as positive. | 实际不是，却被模型说成是。 |
| False negative | 假阴性 / 漏报 | A positive case incorrectly predicted as negative. | 实际是，却被模型漏掉了。 |
| Confusion matrix | 混淆矩阵 | A table counting types of classification outcomes. | 把预测正确、误报、漏报等情况列成表。 |
| Precision-recall trade-off | 精确率-召回率权衡 | Improving one may reduce the other depending on the threshold. | 少误报和少漏报往往不能同时做到最好，需要取舍。 |
| Cost-sensitive learning | 成本敏感学习 | Training or deciding with different error costs. | 把不同错误的代价区别对待。 |
| Class imbalance | 类别不平衡 | Some classes have far fewer examples than others. | 某些类别样本特别少，导致模型容易偏向多数类。 |
| Sampling | 采样 | Selecting data examples for training or evaluation. | 从大量数据中挑选一部分使用。 |
| Data augmentation | 数据增强 | Creating varied training examples from existing data. | 对已有样本做合理变化，生成更多训练例子。 |
| Transfer learning | 迁移学习 | Reusing knowledge learned for one task in another. | 把一个任务学到的能力迁移到新任务。 |
| Self-supervised learning | 自监督学习 | Creating training signals from the data itself. | 不靠人工逐条标答案，而是从数据自身生成学习目标。 |
| Semi-supervised learning | 半监督学习 | Learning from a mix of labeled and unlabeled data. | 一部分数据有答案，另一部分没有答案。 |
| Active learning | 主动学习 | Selecting the most useful examples to label. | 模型主动挑最值得人工标注的数据。 |
| Online learning | 在线学习 | Updating a model as new data arrives. | 新数据不断到来时持续更新模型。 |
| Batch learning | 批量学习 | Training periodically on a collected batch of data. | 收集一批数据后集中训练。 |
| Offline evaluation | 离线评估 | Testing on stored data before or outside live use. | 不接真实用户，先用保存的数据检查模型。 |
| Online evaluation | 在线评估 | Measuring behavior in a live environment. | 模型实际运行时观察真实表现。 |
| A/B test | A/B 测试 | Comparing two system versions with different users or traffic. | 让两种版本分别服务一部分用户，比较谁更好。 |
| Human-in-the-loop | 人在回路 | A workflow where people review or guide model decisions. | 关键环节保留人的判断和干预。 |
| Model update | 模型更新 | Replacing or retraining a deployed model. | 用新数据或新版本重新训练、替换线上模型。 |
| Model drift | 模型漂移 | A deployed model’s performance worsens as conditions change. | 环境变了以后，原来好用的模型逐渐变差。 |
| Model registry | 模型注册库 | A place to track model versions and metadata. | 记录模型版本、状态和说明的管理库。 |
| Versioning | 版本管理 | Tracking changes to data, code, and models. | 记录每次模型和数据改动，方便追踪和回退。 |
| Reproducible pipeline | 可复现流水线 | A pipeline that can be rerun with the same logic. | 同样输入和步骤能重新跑出可比较结果的流程。 |

## Potential Missing Concepts

- The page gives the high-level lifecycle but does not yet explain how a loss function, optimization method, gradient descent, learning rate, or model parameters actually change a model.
- The page names training data and new input, but does not explain dataset splits, held-out data, validation, test data, data leakage, overfitting, underfitting, or generalization in detail.
- The page mentions classification, prediction, ranking, recommendation, and forecasting, but does not distinguish classification from regression or explain common evaluation metrics such as accuracy, precision, recall, F1, MAE, and RMSE.
- The page says “trees and linear models” but does not introduce decision trees, random forests, linear regression, logistic regression, clustering, neural networks, or other algorithm families in detail.
- The page names supervised, unsupervised, reinforcement, and deep learning in surrounding context, but the Machine Learning topic itself does not explain labels, clustering, agents, environments, actions, policies, or rewards.
- The page does not yet cover feature engineering, preprocessing, normalization, missing values, data quality, labeling, class imbalance, or data augmentation.
- The page does not cover deployment, model serving, latency, throughput, monitoring, drift, retraining, versioning, or rollback after a model leaves training.
- The page connects Machine Learning to evaluation, but does not yet cover robustness, fairness, privacy, interpretability, calibration, thresholds, error analysis, or human review.
- The page does not distinguish a model from an algorithm, architecture, parameters, hyperparameters, a database, or a complete product.
- The page uses “pattern” in a beginner-friendly way but does not explain representations, features, embeddings, decision boundaries, probabilities, confidence, or uncertainty.

## Aliases / Synonyms

- Machine Learning / ML / 机器学习
- Artificial Intelligence / AI / 人工智能
- Deep Learning / DL / 深度学习
- Foundation Model / base model / 基础模型 / 基座模型
- trained model / learned model / model / 训练好的模型 / 学习到规律的模型
- training / model fitting / fitting / 训练 / 拟合
- inference / prediction / scoring / 推理 / 预测 / 打分（相关但不完全等同）
- input / feature values / 输入 / 特征值（特征值是输入的一种形式）
- target / expected outcome / ground truth / target answer / 目标值 / 预期结果 / 真实值 / 标准答案（语境不同，不总是严格同义）
- label / class label / category / 标签 / 类别标签 / 类别（label 可是具体答案，class 是类别集合中的一种）
- training data / learning examples / practice examples / 训练数据 / 学习例子 / 练习样本
- new input / unseen data / held-out example / 新输入 / 未见数据 / 留出样本（用途不同，不完全同义）
- classification / categorization / 分类
- regression / numeric prediction / numerical prediction / 回归 / 数值预测
- ranking / ordering / 排序
- recommendation / recommender output / recommendation list / 推荐 / 推荐结果 / 推荐列表
- demand forecast / demand prediction / 需求预测 / 需求预估
- spam filter / spam classifier / junk-mail classifier / 垃圾邮件过滤器 / 垃圾邮件分类器
- rule-based system / fixed-rule programming / symbolic rules / 基于规则的系统 / 固定规则编程 / 符号规则
- model parameters / learned parameters / weights / internal values / 模型参数 / 学到的参数 / 权重 / 内部数值
- hyperparameters / training settings / learning settings / 超参数 / 训练设置 / 学习设置
- evaluation / model assessment / performance measurement / 评估 / 模型评价 / 性能测量
- monitoring / production monitoring / online monitoring / 监控 / 线上监控 / 在线监测
- deployment / productionization / putting a model into production / 部署 / 生产化 / 上线
- model serving / inference serving / prediction service / 模型服务 / 推理服务 / 预测服务
- generalization / performance on unseen data / 泛化 / 在未见数据上的表现
- overfitting / memorization of training data / 过拟合 / 训练数据记忆过度
- underfitting / insufficient learning / 欠拟合 / 学习不足
- neural network / neural net / 神经网络
- multi-layer neural network / deep neural network / 多层神经网络 / 深度神经网络
- decision tree / tree model / 决策树 / 树模型
- linear model / linear predictor / 线性模型 / 线性预测器
- clustering / cluster analysis / 聚类 / 聚类分析
- feedback / reward signal / 反馈 / 奖励信号（强化学习语境下相关但不等同）

## Do Not Confuse Candidates

- Artificial Intelligence vs Machine Learning: AI is the broad field; Machine Learning is one major way to build AI systems.
- Machine Learning vs Deep Learning: Machine Learning is the broader family; Deep Learning is one approach inside it.
- Machine Learning vs fixed-rule programming: Machine Learning learns patterns from examples; fixed-rule programming follows rules explicitly written by a developer.
- Machine Learning vs a model: Machine Learning is the field or process; a model is the learned artifact produced by training.
- Algorithm vs model: An algorithm is a procedure; a model is the learned structure or parameters produced or used by that procedure.
- Training vs inference: Training changes or learns the model; inference applies the learned model to new data.
- Training data vs new input: Training data teaches the model; new input is what the model handles after or outside training.
- Label vs prediction: A label is a known answer attached to an example; a prediction is the model’s returned answer.
- Target vs output: A target is the desired answer used for learning or checking; output is what the model actually returns.
- Score vs probability: A score can be any ranking or comparison number; a probability is intended to represent likelihood and may need calibration.
- Classification vs regression: Classification predicts categories; regression predicts numerical values.
- Prediction vs forecast: A forecast is a prediction specifically about a future value or event; not every prediction is a forecast.
- Ranking vs recommendation: Ranking orders candidates; recommendation presents or selects items, often using ranking underneath.
- Spam filter vs spam classifier: A filter is the product behavior; a classifier is the model or component making the category decision.
- Supervised vs unsupervised learning: Supervised learning uses known labels or target answers; unsupervised learning finds structure without predefined labels.
- Supervised vs reinforcement learning: Supervised learning receives target answers; reinforcement learning receives interaction feedback and rewards.
- Unsupervised vs reinforcement learning: Unsupervised learning discovers structure in data; reinforcement learning learns actions through an environment and rewards.
- Reward vs correct answer: A reward is a feedback signal about an action’s outcome; a correct answer is a target label or value.
- Parameter vs hyperparameter: Parameters are learned from data; hyperparameters are chosen to control the learning process.
- Model parameters vs database records: Parameters encode learned behavior; database records are explicit stored facts or entries.
- Model vs product: A model is one component; a product also includes interface, data, rules, integrations, and operations.
- Foundation Model vs finished product: A foundation model is a reusable starting point; a finished product is a complete user-facing system.
- Foundation Model vs database: A foundation model stores learned statistical behavior in parameters; a database stores explicit records for retrieval.
- Deep Learning vs Neural Network: Deep Learning usually refers to using networks with many layers; a neural network can be small or shallow.
- Deep Learning vs Generative AI: Deep Learning is a method; Generative AI is a goal or application category that often uses Deep Learning.
- Evaluation vs training: Training creates or updates the model; evaluation measures how well it works.
- Validation vs test: Validation helps choose settings or compare versions; test data is reserved for a final check.
- Evaluation vs monitoring: Evaluation is a planned measurement; monitoring watches a deployed system over time.
- Accuracy vs reliability: Accuracy is one metric; reliability is broader consistency and dependability.
- Precision vs recall: Precision focuses on avoiding false positives; recall focuses on finding actual positives.
- Bias vs variance: Bias is systematic error from overly simple assumptions; variance is sensitivity to the particular training data.
- Data drift vs concept drift: Data drift changes input characteristics; concept drift changes the relationship between inputs and outcomes.
- Generalization vs memorization: Generalization works on new cases; memorization mainly repeats training examples.
- Feature vs label: A feature is an input clue; a label is the answer or category to predict.
- Sample vs feature: A sample is one example; a feature is one property of that example.
- Probability vs confidence: A probability has a defined probabilistic interpretation; “confidence” may be an informal score unless calibrated.
- Error vs loss: Error describes a discrepancy for a case; loss is a formal function used to aggregate or optimize discrepancies.
- Model architecture vs model parameters: Architecture is the structural design; parameters are the learned numeric values inside it.
- Model serving vs training: Serving returns predictions for requests; training learns or updates the model.
- Human review vs automatic prediction: Human review adds judgment or approval; automatic prediction returns a model result without that check.
- Pattern discovery vs human understanding: A discovered cluster or correlation is not automatically a meaningful human concept or causal explanation.

## Notes

- Raw collection intentionally keeps broad coverage and repeated or overlapping candidates; do not deduplicate at this stage.
- The primary evidence is the full body of `machine-learning.html`: definition, analogy, training/inference flow, spam filtering, recommendations, demand forecasting, AI/ML/DL distinctions, fixed-rule comparison, related concepts, and video metadata.
- Related-context candidates are drawn from the linked AI Foundations pages and nearby concepts: supervised learning, unsupervised learning, reinforcement learning, deep learning, foundation models, and evaluation.
- Terms such as specific algorithms, metrics, production controls, and safety concepts are retained as review candidates even when the source page only names the category or points to a related concept.
- “Prediction,” “score,” “rank,” and “forecast” are intentionally retained separately because the page presents them as different possible outputs.
- “Training data,” “input,” “expected outcome,” “model,” “new input,” and “prediction” are intentionally retained separately to preserve the five-step flow shown on the source page.
- The page is beginner-oriented, so several English terms have both a precise technical translation and a plain-language explanation for later glossary editing.
