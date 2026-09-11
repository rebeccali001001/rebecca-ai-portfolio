# Topic

Deployment & Operations

## Module / Topic / Source File

- Module: 17 · Product Architecture
- Topic: Deployment & Operations
- Source File: `deployment-operations.html`
- Page description: A beginner-friendly explanation of deployment, hosting, domains, CI/CD, and monitoring.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Deployment & Operations | 部署与运维 | Making a product available and keeping it running. | 把产品发布给用户，并持续让它稳定运行。 |
| deployment | 部署 | Making software available in a target environment. | 把软件放到可以被使用的环境里。 |
| operations | 运维；运营维护 | The work of keeping a live product reliable and usable. | 产品上线后持续维护、观察和处理问题的工作。 |
| product | 产品 | A software experience made available to users. | 用户实际使用的软件或服务。 |
| build a product | 构建产品 | Create and assemble a usable software product. | 把代码和其他部分做成可以使用的产品。 |
| building a product | 构建产品 | The development stage before a product is released. | 产品正式发布前的开发阶段。 |
| release | 发布；上线 | Make a new version available to users. | 把一个新版本交给用户使用。 |
| release path | 发布路径 | The sequence from code to users. | 代码一步步变成用户可用产品的路线。 |
| live product | 在线产品；运行中的产品 | A product currently available to users. | 现在已经在线、用户能使用的产品。 |
| available | 可用；可获得 | Ready for users or systems to access. | 用户或系统能够访问和使用。 |
| users | 用户 | People who use the product. | 使用这个产品的人。 |
| user access | 用户访问 | A user reaching and using the product. | 用户能够打开并使用产品。 |
| code | 代码 | Instructions that implement the product. | 写给电脑执行的程序指令。 |
| CODE | 代码 | The code input at the beginning of the release flow. | 发布流程最开始的代码。 |
| GitHub | GitHub | A service commonly used to store and collaborate on code. | 常用来保存、协作和共享代码的平台。 |
| GITHUB | GitHub | The GitHub step shown in the release path. | 发布路径中保存代码的 GitHub 环节。 |
| repository | 代码仓库 | A managed collection of project files and their history. | 存放项目文件和修改记录的地方。 |
| GitHub repository | GitHub 代码仓库 | A repository hosted on GitHub. | 放在 GitHub 上的代码仓库。 |
| repository step | 代码仓库环节 | The point where code is stored before building. | 代码先保存起来、等待构建的流程环节。 |
| build | 构建 | Turn source code into a runnable or deployable product. | 把源代码加工成能运行或发布的产品。 |
| BUILD | 构建 | The build stage in the release path. | 发布路径中把代码加工成发布物的步骤。 |
| build process | 构建过程 | The operations that prepare software for release. | 为发布准备软件的一组操作。 |
| build artifact | 构建产物 | Files produced by a build and ready for deployment. | 构建后生成、可以拿去部署的文件。 |
| deploy | 部署；发布 | Release the built product to its hosting environment. | 把构建好的产品放到托管环境并发布出去。 |
| DEPLOY | 部署 | The release action in the displayed flow. | 流程图中把产品发布到云或托管环境的动作。 |
| deployment step | 部署步骤 | The point where software is released to an environment. | 把软件真正放到运行环境中的流程步骤。 |
| cloud | 云 | Internet-accessible computing infrastructure. | 通过网络提供计算和存储能力的基础设施。 |
| CLOUD | 云 | The cloud stage shown after deployment. | 发布后承载产品的云基础设施环节。 |
| hosting | 托管 | Providing a place where an application runs. | 给应用提供运行位置和资源。 |
| HOSTING | 托管 | The hosting stage in the release path. | 发布路径中让应用运行的环节。 |
| cloud hosting | 云托管 | Running an application on cloud infrastructure. | 让应用在云服务器或云平台上运行。 |
| hosting environment | 托管环境 | The infrastructure where an application runs. | 应用实际运行的服务器、平台和配置。 |
| application | 应用 | Software that performs a user-facing function. | 为用户提供某种功能的软件。 |
| where the application runs | 应用运行的位置 | The infrastructure location that executes the application. | 应用代码真正运行的地方。 |
| run | 运行 | Execute software so that it can respond to use. | 让软件执行起来并提供功能。 |
| runtime environment | 运行环境 | The software and infrastructure needed to execute an application. | 让应用能够执行的系统、依赖和基础设施。 |
| domain | 域名 | A human-friendly name used to reach a site. | 用户容易记住、用来打开网站的名字。 |
| DOMAIN | 域名 | The domain stage shown in the release path. | 发布路径中让用户访问网站的名称环节。 |
| domain name | 域名名称 | The named address of an internet service. | 互联网上服务的文字地址。 |
| human-friendly address | 便于人记忆的地址 | An address designed for people to read and remember. | 比一串数字更适合人记忆的网站地址。 |
| example.com | example.com | An example of a domain name. | 页面用来演示域名的示例地址。 |
| address | 地址 | A location used to reach a resource. | 用来找到并访问某个资源的位置。 |
| DNS | 域名系统（DNS） | The system that maps domain names to infrastructure locations. | 把域名翻译成实际基础设施位置的系统。 |
| Domain Name System | 域名系统 | The naming system behind DNS lookups. | 负责把网站名字找到对应服务器的系统。 |
| DNS lookup | DNS 查询 | Find the infrastructure destination for a domain. | 查询一个域名应该连接到哪里。 |
| point the domain | 将域名指向 | Configure a domain to lead to a target service. | 设置域名，让它指向实际运行产品的地方。 |
| points the domain to infrastructure | 将域名指向基础设施 | DNS maps the name to the infrastructure serving it. | DNS 把用户输入的网站名指到承载它的基础设施。 |
| infrastructure | 基础设施 | Servers, networks, and services that support an application. | 支撑应用运行的服务器、网络和相关服务。 |
| target infrastructure | 目标基础设施 | The infrastructure selected to receive domain traffic. | 域名最终要连接到的服务器或云服务。 |
| CDN | 内容分发网络（CDN） | A network that delivers content from locations near users. | 在多个地点缓存和发送内容，让用户更快拿到内容。 |
| Content Delivery Network | 内容分发网络 | Distributed infrastructure for efficient content delivery. | 分布在不同地点、专门高效传输内容的网络。 |
| content delivery | 内容分发 | Sending website or application content to users. | 把网页、图片等内容传给用户。 |
| deliver content efficiently | 高效交付内容 | Serve content with suitable speed and location. | 用更合适的地点和方式把内容快速传给用户。 |
| across locations | 跨地点；跨地域 | From multiple geographic or network locations. | 在不同地区或网络位置之间提供服务。 |
| web | Web；互联网 | The networked environment through which sites are accessed. | 用户通过浏览器访问网站的互联网环境。 |
| website | 网站 | A user-facing collection of web pages or functionality. | 用户通过网址访问的网页产品。 |
| site | 站点；网站 | A deployed website or web application. | 已经发布出来的网站或 Web 应用。 |
| users receive new version | 用户获得新版本 | Users are served the newly deployed product version. | 部署完成后，用户访问到更新后的版本。 |
| new version | 新版本 | A newer release of the product. | 相比旧版本更新过的产品版本。 |
| version | 版本 | A particular state of the product over time. | 产品在某个时间点的一套代码和行为。 |
| update | 更新 | Change a live product to a newer state. | 把在线产品换成更新的内容或代码。 |
| UPDATES | 更新 | Ongoing changes that happen alongside the live product. | 产品运行期间持续进行的改动。 |
| monitoring | 监控 | Observe a live system to understand its behavior. | 持续观察线上系统是否正常。 |
| MONITORING | 监控 | Monitoring shown as an activity alongside the live product. | 和线上产品同时进行的持续观察工作。 |
| logging | 日志记录 | Record events and information produced by a system. | 把系统发生的事情记录下来，方便排查。 |
| LOGGING | 日志记录 | Logging shown as an activity alongside the live product. | 产品运行时同步收集系统记录。 |
| live product operations | 线上产品运维 | Monitoring, logging, and updating a running product. | 产品上线后围绕运行、记录和更新进行维护。 |
| alongside | 同时进行；伴随 | Happening at the same time as another activity. | 和产品运行同时发生，而不是只在发布前做。 |
| available, observable, and maintainable | 可用、可观测、可维护 | Three qualities of a product kept in operation. | 产品要能用、看得见状态、也方便维护。 |
| observable | 可观测的 | Able to reveal useful information about its behavior. | 系统的运行状态和问题能被看见和分析。 |
| maintainable | 可维护的 | Easy enough to update, repair, and operate over time. | 以后容易修改、修复和持续管理。 |
| release it there | 将其发布到那里 | Put the application in the hosting location. | 把应用发布到前面说的托管环境中。 |
| process of releasing | 发布过程 | The steps used to make software available in a target place. | 把软件放到目标环境并让用户使用的一连串步骤。 |
| hosting vs deployment | 托管与部署的区别 | Hosting is the place; deployment is the release process. | 托管是“放在哪里运行”，部署是“怎么发布过去”。 |
| hosting versus deployment | 托管与部署对比 | A comparison between runtime location and release action. | 对比应用运行的位置和把应用发布过去的动作。 |
| release path: CODE | 发布路径：代码 | The starting material for a release. | 发布流程从项目代码开始。 |
| release path: GITHUB / REPOSITORY | 发布路径：GitHub / 代码仓库 | The place where code is stored before the build. | 代码先放进 GitHub 或代码仓库。 |
| release path: BUILD | 发布路径：构建 | The stage that prepares code for deployment. | 把代码加工成可以部署的产物。 |
| release path: DEPLOY | 发布路径：部署 | The stage that releases the prepared product. | 把准备好的产品发布到运行环境。 |
| release path: CLOUD / HOSTING | 发布路径：云 / 托管 | The environment that runs the deployed product. | 云或托管平台承载已经部署的产品。 |
| release path: DOMAIN | 发布路径：域名 | The user-facing name used to reach the product. | 用户通过域名找到产品。 |
| release path: USERS | 发布路径：用户 | The people who ultimately use the release. | 最终使用发布结果的人。 |
| flow | 流程；流向 | An ordered movement through stages. | 按先后顺序经过的一组步骤。 |
| process node | 流程节点 | One meaningful stage in a process. | 流程中的一个关键步骤或站点。 |
| code-to-user flow | 从代码到用户的流程 | The full route from source code to user access. | 代码经过构建、部署和访问后到达用户。 |
| live product path | 在线产品路径 | The stages that lead to a product users can access. | 让产品从代码变成用户能访问的在线服务的路线。 |
| CI/CD | 持续集成/持续交付或部署（CI/CD） | Automation that helps test, build, and release code changes. | 代码一改动，就自动测试、构建并可发布的一套做法。 |
| Continuous Integration | 持续集成 | Frequently combine code changes and test them. | 经常把代码改动合并，并自动检查有没有问题。 |
| Continuous Delivery | 持续交付 | Keep software ready to release through automation. | 让软件随时处于可以发布的准备状态。 |
| Continuous Deployment | 持续部署 | Automatically release a change after it passes the pipeline. | 代码通过自动检查后，自动发布到线上。 |
| What Is CI/CD? | 什么是 CI/CD？ | A section explaining the CI/CD release automation idea. | 页面用来解释 CI/CD 自动化发布的部分。 |
| code change | 代码变更 | A modification made to the project code. | 开发者对项目代码做的一次修改。 |
| CODE CHANGE | 代码变更 | The first stage in the CI/CD flow. | CI/CD 流程从代码修改开始。 |
| test | 测试 | Check whether software behaves as expected. | 检查软件是否按预期工作。 |
| TEST / BUILD | 测试 / 构建 | The combined checking and preparation stage in CI/CD. | CI/CD 中先检查代码，再准备发布物的阶段。 |
| testing | 测试 | The activity of checking a code change or product. | 对代码或产品进行检查的活动。 |
| build after change | 变更后的构建 | Build the product after code has changed. | 代码改完后重新生成可发布版本。 |
| deploy after build | 构建后的部署 | Release the result after it has been built. | 构建成功后把结果发布到线上。 |
| automate | 自动化 | Make a task happen through software with less manual work. | 让系统自动完成原本需要人手动做的步骤。 |
| automates parts of testing | 自动化部分测试 | CI/CD performs some testing automatically. | CI/CD 自动完成测试工作中的一部分。 |
| automates parts of releasing software | 自动化部分软件发布 | CI/CD performs some release steps automatically. | CI/CD 自动完成软件发布工作中的一部分。 |
| software release | 软件发布 | Making a software version available in its target environment. | 把某个软件版本放到目标环境供使用。 |
| release automation | 发布自动化 | Automated steps that prepare and release software. | 用自动化流程测试、构建和发布软件。 |
| CI/CD pipeline | CI/CD 流水线 | An automated sequence from code change to release. | 从代码改动一路自动走到部署的流程。 |
| pipeline | 流水线 | A connected sequence of automated processing stages. | 多个按顺序连接、自动执行的步骤。 |
| trigger | 触发 | Cause an automated process to start. | 让自动流程开始运行的事件或动作。 |
| build triggered | 构建被触发 | A change causes the build stage to start. | 代码变化后，构建流程自动开始。 |
| BUILD TRIGGERED | 构建被触发 | The third step in the real example. | 页面示例中第三步：系统开始构建。 |
| automatic trigger | 自动触发 | Start a process without a person manually launching it. | 不需要人点击启动，系统自己开始流程。 |
| code-to-deploy automation | 从代码到部署的自动化 | Automate the stages between a code change and deployment. | 把代码修改到最终部署之间的步骤自动串起来。 |
| release software | 发布软件 | Make a software build available to users. | 把软件版本交给用户使用。 |
| deployment flow | 部署流程 | An ordered sequence used to deploy software. | 按顺序进行构建、部署和上线的一套步骤。 |
| process flow | 流程图；流程流 | A visual or conceptual sequence of process steps. | 用步骤展示一件事怎样从开始走到结束。 |
| step | 步骤 | One action in an ordered process. | 流程中先后顺序明确的一步。 |
| step 01 | 第 01 步 | The first step in the example sequence. | 示例发布流程的第一步。 |
| step 02 | 第 02 步 | The second step in the example sequence. | 示例发布流程的第二步。 |
| step 03 | 第 03 步 | The third step in the example sequence. | 示例发布流程的第三步。 |
| step 04 | 第 04 步 | The fourth step in the example sequence. | 示例发布流程的第四步。 |
| step 05 | 第 05 步 | The fifth step in the example sequence. | 示例发布流程的第五步。 |
| developer | 开发者 | A person who changes and maintains software code. | 编写、修改和维护软件代码的人。 |
| developer updates website | 开发者更新网站 | A developer changes the website code or content. | 开发者先修改网站的代码或内容。 |
| updates website | 更新网站 | Changes are made to the website. | 对网站进行修改和更新。 |
| push | 推送 | Send local code changes to a shared repository. | 把本地改动上传到共享代码仓库。 |
| Push to GitHub | 推送到 GitHub | Send the code change to GitHub. | 把改好的代码提交并上传到 GitHub。 |
| cloud deployment | 云部署 | Release an application to cloud infrastructure. | 把应用发布到云平台运行。 |
| Cloudflare | Cloudflare | A provider that can deliver and deploy web properties. | 页面示例中负责部署网站的云服务提供商之一。 |
| Vercel | Vercel | A platform that can build and deploy web applications. | 页面示例中负责部署网站的托管和发布平台之一。 |
| Cloudflare / Vercel | Cloudflare / Vercel | Example services that deploy the site. | 页面列出的两个网站部署服务示例。 |
| deploys site | 部署网站 | A platform releases the site to its hosting environment. | 平台把网站发布到可以访问的线上环境。 |
| site deployment service | 网站部署服务 | A service that handles some or all website deployment steps. | 帮助把网站构建并发布到线上的服务。 |
| user-facing site | 面向用户的网站 | A site that users can visit and use. | 最终给用户打开和使用的网站。 |
| after release | 发布之后 | The period when the product is live for users. | 产品已经上线、开始被用户使用之后。 |
| monitoring after release | 发布后监控 | Observe the product after it becomes live. | 上线后持续检查产品是否正常。 |
| production | 生产环境；线上环境 | The live environment serving real users. | 真正服务用户的线上运行环境。 |
| production behavior | 生产环境行为；线上行为 | How the system behaves while serving real users. | 系统在线上真实运行时表现出来的行为。 |
| understand production behavior | 了解线上行为 | Use monitoring information to learn how the live system behaves. | 通过监控知道真实用户使用时系统表现如何。 |
| online | 在线 | Reachable and operating on the internet. | 已经连上网络并且能够访问。 |
| IS IT ONLINE? | 是否在线？ | A monitoring question about availability. | 监控首先要确认产品还能不能打开。 |
| availability | 可用性 | Whether a service is reachable and functioning. | 服务在需要时能不能访问和工作。 |
| uptime | 正常运行时间；在线率 | The amount or proportion of time a service is available. | 服务保持在线、可用的时间或比例。 |
| request | 请求 | A call from a user or client asking a service to do something. | 用户或程序向服务发出的一个访问要求。 |
| requests failing | 请求失败 | Requests do not complete successfully. | 用户发出的访问没有成功完成。 |
| ARE REQUESTS FAILING? | 请求是否失败？ | A monitoring question about failed requests. | 监控要检查访问请求有没有出错。 |
| request failure | 请求失败 | A request ends unsuccessfully. | 一次访问请求没有得到正常结果。 |
| request failure rate | 请求失败率 | The proportion of requests that fail. | 所有请求中失败请求占的比例。 |
| error | 错误 | A problem reported by the system or experienced by a user. | 系统或用户遇到的异常问题。 |
| errors | 错误（复数） | Multiple error conditions or messages. | 一个或多个系统错误或报错信息。 |
| users seeing errors | 用户看到错误 | Users receive or observe error states. | 用户界面或使用过程中出现报错。 |
| ARE USERS SEEING ERRORS? | 用户是否看到错误？ | A monitoring question about user-visible failures. | 监控要检查用户实际有没有看到错误。 |
| user-visible error | 用户可见错误 | An error exposed directly to a user. | 用户能在页面或操作结果中直接看到的错误。 |
| slow | 慢 | Taking longer than users or the system expect. | 响应时间太长，让用户感觉卡顿。 |
| IS IT SLOW? | 是否变慢？ | A monitoring question about performance. | 监控要确认产品响应是不是变慢了。 |
| speed | 速度 | How quickly a system responds or delivers content. | 系统响应或内容传输有多快。 |
| latency | 延迟 | The time between a request and its response. | 从发出请求到收到回应所等待的时间。 |
| response time | 响应时间 | The time a system takes to answer a request. | 系统处理请求并返回结果所用的时间。 |
| performance | 性能 | How well and quickly the system operates. | 系统运行速度、稳定性等整体表现。 |
| monitoring signal | 监控信号 | A piece of observed information about system behavior. | 用来判断系统状态的一项观察信息。 |
| production monitoring | 生产环境监控 | Monitoring a system that serves real users. | 观察正在服务真实用户的线上系统。 |
| service health | 服务健康状态 | An assessment of whether the service is operating normally. | 判断服务目前是否正常工作的状态。 |
| operational health | 运维健康状态 | The overall operating condition of a live product. | 线上产品整体是否稳定、可用、可维护。 |
| failure | 失败；故障 | A requested operation does not complete correctly. | 某个操作没有按预期完成。 |
| incident | 事故；线上事件 | An operational event that requires attention or response. | 线上出现需要处理的异常事件。 |
| alert | 告警 | A notification that a monitored condition needs attention. | 系统发现异常后发出的提醒。 |
| observability | 可观测性 | The ability to understand system state from its outputs and signals. | 通过日志、指标等信息判断系统内部发生了什么。 |
| maintenance | 维护 | Work that keeps software usable and up to date. | 让软件持续能用并保持更新的工作。 |
| maintain | 维护 | Operate, repair, and update a live product. | 持续运行、修复和更新线上产品。 |
| reliability | 可靠性 | The ability to keep working correctly over time. | 长时间稳定、正确工作的能力。 |
| reliable | 可靠的 | Consistently available and functioning as expected. | 能持续按预期工作，不容易出故障。 |
| keep it running reliably | 可靠地保持运行 | Operate the product with consistent service behavior. | 让产品长期稳定地运行。 |
| keep it available | 保持可用 | Ensure users can reach and use the product. | 确保用户一直能够访问和使用。 |
| keep it observable | 保持可观测 | Preserve useful signals about system behavior. | 确保系统状态持续能被监控和分析。 |
| keep it maintainable | 保持可维护 | Keep the product easy to update and repair. | 让产品以后仍然容易修改和修复。 |
| real example | 实际示例 | One concrete sequence showing how deployment can happen. | 页面用一个具体案例展示发布过程。 |
| One real example | 一个实际示例 | A concrete example of a deployment path. | 对某种部署路径的具体演示。 |
| example architecture | 示例架构 | One possible arrangement of product and deployment components. | 产品和发布组件的一种组织方式。 |
| not the only architecture | 不是唯一架构 | The example is illustrative, not a universal design. | 这个例子只是其中一种做法，不代表所有系统都一样。 |
| architecture | 架构 | The arrangement of components and operational stages. | 产品各部分如何组合、运行和发布的整体设计。 |
| new release | 新发布版本 | A version made available through a release. | 经过发布后交给用户的新版本。 |
| receive | 接收；获得 | Be served or obtain a product version. | 用户访问时拿到某个版本的产品。 |
| deploys | 部署（第三人称） | Releases an application to an environment. | 把应用发布到运行环境的动作。 |
| operations keep it running | 运维让产品持续运行 | Operations preserve the service after release. | 产品发布后靠运维继续保持正常工作。 |
| deployment releases a product to users | 部署把产品发布给用户 | Deployment makes a product available to its audience. | 部署就是让用户真正用到产品。 |
| product availability | 产品可用性 | Whether users can access the released product. | 用户能不能访问到已经发布的产品。 |
| operational process | 运维流程 | A repeatable set of activities for running a product. | 持续运行产品时反复执行的一组工作。 |
| release management | 发布管理 | Coordinate versions, release steps, and availability. | 管理版本、发布步骤和上线结果。 |
| infrastructure management | 基础设施管理 | Operate the resources that host the application. | 管理承载应用的服务器、网络和云资源。 |
| domain routing | 域名路由 | Direct a domain’s traffic to the right service. | 把域名访问流量引到正确的服务。 |
| traffic | 流量 | Requests sent by users or clients to a service. | 用户和程序访问服务产生的请求量。 |
| content | 内容 | Files or responses delivered by a website or application. | 网站或应用要交给用户的文字、图片等信息。 |
| software | 软件 | Programs and related files that perform useful work. | 让电脑完成任务的程序和文件。 |
| task | 任务 | A piece of work performed by a person or system. | 人或系统需要完成的一件工作。 |
| process of releasing it there | 将应用发布到托管处的过程 | The deployment process from prepared software to hosting. | 把应用放到托管环境并使其运行起来的过程。 |
| parts of testing | 测试环节的一部分 | Some, but not necessarily all, testing activities. | 测试流程中的部分工作。 |
| parts of releasing | 发布环节的一部分 | Some, but not necessarily all, release activities. | 发布流程中的部分工作。 |
| live | 在线运行的 | Currently running and serving users. | 当前正在运行并服务用户。 |
| operation | 运行维护；操作 | An activity or condition involved in running software. | 与软件运行或维护有关的活动或状态。 |

## Potential Missing Concepts

- The page introduces deployment and operations at a high level but does not explain environments such as local development, staging, preview, and production in detail.
- It does not define source control, Git commits, branches, pull requests, merge checks, or how a GitHub repository records code history.
- It names build and deploy but does not explain build artifacts, dependency installation, environment variables, secrets, configuration, runtime dependencies, or build failures.
- It does not describe deployment strategies such as rolling deployment, blue-green deployment, canary release, feature flags, immutable deployment, or rollback.
- It does not explain what happens when a deployment fails, how to recover, or how to roll back to a previous version.
- It introduces CI/CD but does not distinguish continuous integration, continuous delivery, and continuous deployment in operational detail.
- It does not cover pipeline stages such as linting, unit tests, integration tests, end-to-end tests, security scans, approvals, artifact storage, or promotion between environments.
- It does not explain hosting resource types such as servers, virtual machines, containers, serverless functions, managed platforms, object storage, or databases.
- It does not cover infrastructure as code, provisioning, configuration management, autoscaling, load balancing, health checks, or resource capacity.
- It mentions cloud and hosting but does not explain regions, availability zones, networking, firewall rules, ports, TLS/HTTPS, certificates, or private versus public access.
- It names domain and DNS but does not explain DNS records, nameservers, A/AAAA records, CNAME records, TTL, propagation, redirects, or domain registration.
- It names CDN but does not explain edge locations, caching, cache invalidation, origin servers, cache-control headers, or static versus dynamic content.
- It uses monitoring questions but does not define concrete metrics, dashboards, logs, traces, metrics collection, alert thresholds, alert routing, or on-call response.
- It suggests online status, failed requests, slowness, and user errors but does not define uptime, availability targets, error rate, latency percentiles, throughput, saturation, or service-level objectives.
- It does not explain the difference between monitoring and observability, or how logs, metrics, and traces complement one another.
- It does not cover incident management, severity, escalation, runbooks, postmortems, status communication, or recovery time objectives.
- It does not explain application logs versus infrastructure logs, structured logging, log levels, log retention, correlation IDs, or privacy-sensitive logging.
- It does not cover security operations such as access control, secret rotation, dependency patching, vulnerability scanning, WAFs, DDoS protection, or audit trails.
- It does not cover backups, disaster recovery, replication, restore testing, business continuity, or recovery point and recovery time objectives.
- It does not explain data migrations, schema compatibility, stateful services, database releases, or how to coordinate application and data changes.
- It does not discuss cost monitoring, usage limits, quotas, billing alerts, capacity planning, or cloud-provider lock-in.
- It does not distinguish a website, web application, API service, background worker, static asset, and full product architecture.
- It mentions Cloudflare and Vercel only as examples and does not explain their exact responsibilities, trade-offs, or alternatives.
- It does not explain request routing from a browser through DNS, CDN, load balancer, application runtime, and backend services.
- It does not explain cache behavior, stale content, browser caching, CDN caching, or what users may see during propagation.
- It does not explain version identification, release notes, change tracking, auditability, or reproducibility of a release.
- It does not cover testing after deployment, smoke tests, health-check endpoints, synthetic monitoring, or user acceptance checks.
- It does not explain how to measure user-visible errors separately from internal errors or how to connect an error to a specific release.
- It does not cover performance optimization, latency budgets, concurrency, throughput, queueing, rate limiting, retries, timeouts, or circuit breakers.
- It does not cover operational ownership, on-call rotations, support workflows, service catalogs, or responsibility boundaries between development and operations.
- It does not explain maintenance windows, planned downtime, backward compatibility, deprecation, or end-of-life procedures.

## Aliases / Synonyms

- deployment / deploy / release / rollout / 上线 / 部署 / 发布 / 发布上线（相关，但 rollout 可强调逐步放量）
- operations / ops / IT operations / 运维 / 运营维护
- hosting / application hosting / cloud hosting / 托管 / 应用托管 / 云托管
- hosting environment / runtime environment / execution environment / 托管环境 / 运行环境 / 执行环境（范围可能不同）
- application / app / software application / 应用 / 应用程序
- product / software product / digital product / 产品 / 软件产品 / 数字产品
- code / source code / program code / 代码 / 源代码 / 程序代码
- repository / code repository / source repository / 代码仓库 / 源代码仓库
- GitHub / GitHub repository / Git repo on GitHub / GitHub / GitHub 代码仓库 / GitHub 上的 Git 仓库
- build / compile / package / construct / 构建 / 编译 / 打包（不完全同义）
- build artifact / build output / release artifact / 构建产物 / 构建输出 / 发布产物
- deploy / publish / release / put into production / 部署 / 发布 / 上线 / 投产
- live / online / in production / serving users / 在线 / 线上 / 生产中 / 服务用户中
- cloud / cloud infrastructure / cloud platform / 云 / 云基础设施 / 云平台
- domain / domain name / web address / 域名 / 域名名称 / 网站地址
- human-friendly address / readable address / memorable address / 便于人阅读的地址 / 易记地址
- DNS / Domain Name System / 域名系统 / DNS / Domain Name System / 域名系统
- DNS lookup / name resolution / domain resolution / DNS 查询 / 名称解析 / 域名解析
- point a domain to infrastructure / route a domain / map a domain / 将域名指向基础设施 / 路由域名 / 映射域名
- infrastructure / hosting infrastructure / runtime infrastructure / 基础设施 / 托管基础设施 / 运行基础设施
- CDN / Content Delivery Network / edge delivery network / 内容分发网络 / 边缘交付网络
- content delivery / serving content / delivering assets / 内容分发 / 提供内容 / 交付资源
- CI/CD / delivery pipeline / release pipeline / CI/CD / 交付流水线 / 发布流水线
- CI / Continuous Integration / 持续集成 / Continuous Integration
- CD / Continuous Delivery / Continuous Deployment / 持续交付 / 持续部署（CD 具体含义依上下文）
- code change / code update / source change / 代码变更 / 代码更新 / 源代码改动
- test / testing / verification / check / 测试 / 检查 / 验证
- trigger a build / start a build / build automatically / 触发构建 / 启动构建 / 自动构建
- pipeline / workflow / automated flow / 流水线 / 工作流 / 自动化流程
- automate / automate a step / run automatically / 自动化 / 自动执行 / 自动运行
- monitoring / production monitoring / online monitoring / 监控 / 生产环境监控 / 线上监控
- logging / log collection / event logging / 日志记录 / 日志收集 / 事件记录
- observability / system visibility / operational visibility / 可观测性 / 系统可见性 / 运维可见性
- available / accessible / reachable / available to users / 可用 / 可访问 / 可到达 / 对用户可用
- availability / uptime / service availability / 可用性 / 正常运行时间 / 服务可用性（ uptime 是时间或比例表达）
- request / client request / service call / 请求 / 客户端请求 / 服务调用
- request failure / failed request / unsuccessful request / 请求失败 / 失败请求 / 未成功请求
- error / failure / fault / problem / 错误 / 失败 / 故障 / 问题（技术语境不完全相同）
- user-visible error / user-facing error / visible error / 用户可见错误 / 面向用户的错误 / 可见错误
- slow / high latency / poor response time / 慢 / 高延迟 / 响应时间差
- latency / response time / waiting time / 延迟 / 响应时间 / 等待时间
- performance / speed / responsiveness / 性能 / 速度 / 响应性
- maintainable / easy to maintain / operable over time / 可维护的 / 易于维护的 / 可长期运维的
- reliable / dependable / consistently working / 可靠的 / 稳定可信的 / 持续正常工作的
- production behavior / live behavior / runtime behavior / 线上行为 / 在线行为 / 运行时行为
- real example / concrete example / illustrative example / 实际示例 / 具体示例 / 说明性示例
- architecture / deployment architecture / system arrangement / 架构 / 部署架构 / 系统组织方式
- new version / updated version / latest release / 新版本 / 更新版本 / 最新发布版本
- update / change / revision / 更新 / 改动 / 修订
- users receive new version / users get the release / users are served the new build / 用户获得新版本 / 用户拿到发布版本 / 用户访问到新构建

## Do Not Confuse Candidates

- Deployment vs hosting: deployment is the process of releasing software; hosting is the place and resources where it runs.
- Deployment vs release: the page uses them closely, but deployment emphasizes placing software in an environment while release emphasizes making a version available to users.
- Deployment vs update: deployment can be an update, but an update is any change and does not necessarily describe the full deployment process.
- Operations vs development: development creates or changes software; operations keeps the live product available, observable, reliable, and maintainable.
- Hosting environment vs production environment: a hosting environment is where software runs; production is the live environment serving real users.
- Cloud vs hosting: cloud is a broad infrastructure model or platform category; hosting is the service of running an application in a place.
- Code vs build: code is the source input; a build is the prepared output or process that turns code into something deployable.
- Build vs deploy: build prepares the product; deploy releases the prepared product to its environment.
- Build artifact vs source code: an artifact is generated from source code and is intended for execution or deployment.
- Repository vs deployment environment: a repository stores code and history; a deployment environment runs the application.
- GitHub vs repository: GitHub is a service; a repository is the project collection stored on that service.
- Push vs deploy: pushing sends code to a repository; deploying makes a version run in a hosting environment.
- Domain vs DNS: a domain is the human-friendly name; DNS is the system that resolves the name to infrastructure.
- Domain vs URL: a domain is a naming component; a URL can include scheme, domain, path, query, and fragment.
- DNS vs CDN: DNS directs a name to an endpoint; a CDN delivers content through distributed locations.
- DNS vs domain registration: DNS controls resolution; registration reserves ownership or control of a domain name.
- CDN vs hosting: a CDN distributes or caches delivery; hosting provides the origin environment where the application or content runs.
- CDN vs origin server: a CDN may serve cached content; the origin is the source service it fetches from when needed.
- Online vs available: online often means reachable or running; available usually includes being usable and responding successfully.
- Availability vs uptime: availability is a service-quality concept; uptime is commonly the amount or percentage of time the service is up.
- Monitoring vs logging: monitoring observes health and behavior; logging records events and details that can be inspected.
- Monitoring vs observability: monitoring checks known conditions; observability is the broader ability to infer internal state from system signals.
- Logging vs metrics: logs are event records; metrics are numeric measurements tracked over time.
- Error vs failure: an error may be a message or condition; failure is an operation not completing successfully.
- Internal error vs user-visible error: an internal error may remain hidden; a user-visible error directly affects what the user sees.
- Request failure vs application outage: some requests can fail while the service remains partly available; an outage is a broader loss of service.
- Slow vs unavailable: a slow service responds with delay; an unavailable service cannot be reached or completed successfully.
- Latency vs throughput: latency is time per request; throughput is how much work or traffic is handled per unit of time.
- Speed vs reliability: speed concerns how quickly a response arrives; reliability concerns consistent correct operation over time.
- CI vs CD: CI focuses on integrating and testing changes; CD covers keeping changes ready for delivery or automatically deploying them.
- Continuous delivery vs continuous deployment: delivery may require a release decision; deployment automatically sends an approved change to an environment.
- CI/CD pipeline vs deployment: a pipeline is the automated sequence; deployment is one action or outcome within that sequence.
- Test vs monitoring: tests check expected behavior at planned points; monitoring watches real behavior over time.
- Code change vs new version: a code change is an edit; a new version is a packaged or released state that may contain one or many changes.
- Trigger vs build: a trigger starts a build; the build performs the preparation work.
- Automation vs autonomy: automation follows configured steps; autonomy may involve a system making broader decisions, which this page does not imply.
- Production behavior vs test behavior: production behavior comes from real use; test behavior comes from controlled checks.
- User receives a version vs user downloads a file: a user may be served a version through a site without directly downloading the deployment artifact.
- Website vs site deployment: a website is the user-facing product; site deployment is the process that makes it available.
- Product vs application: a product may include an application plus data, infrastructure, integrations, and operations; an application is one software component or experience.
- Architecture vs example architecture: architecture is the overall arrangement; the page’s example is only one possible arrangement.
- Cloudflare vs Vercel: both can participate in web delivery or deployment, but they are different providers with different capabilities and operational models.
- Cloudflare / Vercel vs hosting in general: the named providers are examples, not definitions of all hosting or deployment architectures.
- Release path vs architecture: the release path shows sequence; architecture describes components and their relationships.
- Update vs maintenance: an update changes a product; maintenance is the broader ongoing work of keeping it healthy.
- Reliability vs maintainability: reliability is consistent operation; maintainability is ease of repair and change.
- Available vs observable: a service can be available but poorly observable; users can access it even when operators cannot easily understand its state.
- Observable vs maintainable: observability helps diagnose behavior; maintainability concerns how easily the system can be changed or repaired.
- Domain routing vs application routing: domain routing gets traffic to an endpoint; application routing chooses behavior or resources inside the application.
- Content delivery vs application execution: a CDN may deliver cached content; application execution runs code to generate or process responses.
- Real example vs prescribed architecture: the five-step example demonstrates one route and is explicitly not the only architecture.

## Notes

- Raw collection intentionally preserves repeated, overlapping, synonymous, and differently capitalized candidates from the full body; do not deduplicate at this stage.
- The source body contains the visible sequence `CODE → GITHUB / REPOSITORY → BUILD → DEPLOY → CLOUD / HOSTING → DOMAIN → USERS`; each process node and several combined labels are retained separately.
- The source repeats operational activities as `MONITORING · LOGGING · UPDATES`; the candidates preserve both title-case concepts and the operational phrases built from them.
- The source explicitly contrasts `HOSTING` (“Where the application runs”) with `DEPLOYMENT` (“The process of releasing it there”); these must remain separate in later glossary editing.
- The page presents `DOMAIN`, `DNS`, and `CDN` as separate web concepts: a human-friendly address, infrastructure pointing, and efficient cross-location content delivery.
- CI/CD is retained as an abbreviation and expanded into Continuous Integration, Continuous Delivery, and Continuous Deployment candidates for later review, even though the source gives only a high-level automation explanation.
- The monitoring questions are retained as phrase-level candidates because they imply operational indicators: online status/availability, failed requests/request failure rate, slowness/latency, and user-visible errors.
- `Cloudflare / Vercel` is retained as a provider/example candidate, not as a claim that every deployment uses either provider.
- The real example is explicitly marked as “one example, not the only architecture”; the example sequence is therefore evidence for candidate collection, not a universal deployment prescription.
- Candidate descriptions are beginner-friendly paraphrases for later glossary review, not a claim that every phrase is a formal standards term.
- The source page is `deployment-operations.html`; this file does not modify the source website or any GitHub repository.
