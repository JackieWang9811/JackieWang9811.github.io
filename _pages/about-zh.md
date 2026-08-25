---
permalink: /zh/
title: ""
excerpt: "关于我"
author_profile: true
lang: zh-CN
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<span id="about-me" class="anchor-target"></span>
<nav class="language-switch" aria-label="语言切换">
  <a href="/">English</a>
  <span>中文</span>
</nav>

你好！我是**王嘉琪**，英文名 Jackie，目前是[哈尔滨工业大学（深圳）](https://www.hitsz.edu.cn/)（HITSZ）与[鹏城实验室](https://www.pcl.ac.cn/)（PCL）联合培养的计算机科学与技术专业博士研究生，导师为[张治国教授](https://scholar.google.com/citations?hl=en&user=DAtNH6EAAAAJ&view_op=list_works&sortby=pubdate)和[马铮宇教授](https://scholar.google.com/citations?hl=en&user=21SR930AAAAJ&view_op=list_works&sortby=pubdate)。

我的研究关注类脑智能、脉冲神经网络以及神经/语音信号解码，代表性项目包括 [CET-MAE](https://github.com/JackieWang9811/CET-MAE)、[S^2M-Former](https://github.com/JackieWang9811/S2M-Former)、[SpikeSCR](https://github.com/JackieWang9811/SpikeSCR) 和 [SpikCommander](https://github.com/JackieWang9811/SCommander)。

我硕士毕业于[吉林大学](https://www.jlu.edu.cn/)控制科学与工程专业，导师为[陈万忠教授](https://dce.jlu.edu.cn/info/1182/9723.htm)。本科毕业于[东北电力大学](http://www.neepu.edu.cn/)自动化专业，导师为沈学强副教授。

我的中文简历：**[王嘉琪简历（CN）](../assets/WJQ_CV_CN.pdf)**。

{% assign metrics = site.data.profile_metrics %}
[Google Scholar](https://scholar.google.com.hk/citations?hl=zh-CN&tzom=-480&user=jz4IkO0AAAAJ){% if metrics.google_scholar_citations %} (<span data-profile-metric="google_scholar_citations">{{ metrics.google_scholar_citations }}</span> 次引用){% endif %} /
[GitHub](https://github.com/JackieWang9811){% if metrics.github_stars %} (<span data-profile-metric="github_stars">{{ metrics.github_stars }}</span> stars){% endif %} /
[CSDN](https://blog.csdn.net/jq_98){% if metrics.csdn_views %} (<span data-profile-metric="csdn_views">{{ metrics.csdn_views }}</span> 访问){% endif %} /

<script defer src="/assets/js/profile-metrics.js"></script>

**Email**: mhwjq1998@gmail.com; **WeChat**: JackieWang9811

---

### 🔍 研究方向

我的研究主要关注：
- **脉冲神经网络（SNN）**
- **时序与序列建模**
- **脑机接口（BCI）**
- **语音与语言模型**

---

### 🤝 合作交流

我希望推动类脑智能以及**语音**和**神经**信号（EEG、ECG、EMG）解码技术的发展。  
如果你正在研究 SNN、BCI 解码、时序建模或高效神经网络架构，非常欢迎交流与合作！

欢迎通过邮件联系我。😊

**Coming soon:** 还有三篇论文正在路上，敬请期待！

## 🌟 代表项目
{: #featured-projects .section-title }

<div class="project-grid">
  <article class="project-card">
    <div class="project-card__top">
      <span class="project-card__venue">AAAI 2026</span>
      <span class="project-card__stars">★ <span data-github-stars="JackieWang9811/SCommander">14</span></span>
    </div>
    <h3>SpikCommander</h3>
    <p>面向高效语音命令识别的高性能脉冲 Transformer。</p>
    <div class="project-card__tags">
      <span>SNN</span><span>Speech</span><span>Transformer</span>
    </div>
    <div class="project-card__links">
      <a href="https://arxiv.org/abs/2511.07883v1">Paper</a>
      <a href="https://github.com/JackieWang9811/SCommander">Code</a>
    </div>
  </article>

  <article class="project-card">
    <div class="project-card__top">
      <span class="project-card__venue">NeurIPS 2025</span>
      <span class="project-card__stars">★ <span data-github-stars="JackieWang9811/S2M-Former">7</span></span>
    </div>
    <h3>S<sup>2</sup>M-Former</h3>
    <p>用于脑听觉注意检测的脉冲对称混合 Branchformer。</p>
    <div class="project-card__tags">
      <span>EEG</span><span>BCI</span><span>Attention</span>
    </div>
    <div class="project-card__links">
      <a href="https://arxiv.org/abs/2508.05164">Paper</a>
      <a href="https://github.com/JackieWang9811/S2M-Former">Code</a>
    </div>
  </article>

  <article class="project-card">
    <div class="project-card__top">
      <span class="project-card__venue">Neural Networks</span>
      <span class="project-card__stars">★ <span data-github-stars="JackieWang9811/SpikeSCR">7</span></span>
    </div>
    <h3>SpikeSCR</h3>
    <p>结合脉冲神经网络与课程蒸馏的高效语音命令识别方法。</p>
    <div class="project-card__tags">
      <span>SNN</span><span>Distillation</span><span>Efficient AI</span>
    </div>
    <div class="project-card__links">
      <a href="https://arxiv.org/abs/2412.12858">Paper</a>
      <a href="https://github.com/JackieWang9811/SpikeSCR">Code</a>
    </div>
  </article>

  <article class="project-card">
    <div class="project-card__top">
      <span class="project-card__venue">ACL 2024</span>
      <span class="project-card__stars">★ <span data-github-stars="JackieWang9811/CET-MAE">14</span></span>
    </div>
    <h3>CET-MAE</h3>
    <p>面向 EEG-to-Text 解码的对比式 EEG-文本掩码自编码预训练。</p>
    <div class="project-card__tags">
      <span>EEG-to-Text</span><span>MAE</span><span>Representation</span>
    </div>
    <div class="project-card__links">
      <a href="https://arxiv.org/abs/2402.17433">Paper</a>
      <a href="https://github.com/JackieWang9811/CET-MAE">Code</a>
    </div>
  </article>
</div>

## 📝 代表性成果
{: #publications .section-title }

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">AAAI 2026</span> [
SpikCommander: A High-performance Spiking Transformer with Multi-view Learning for Efficient Speech Command Recognition](https://arxiv.org/abs/2511.07883v1),
   <ins>**Jiaqi Wang**</ins>, Liutao Yu, Xiongri Shen, Sihang Guo, Chenlin Zhou, Leilei Zhao, Yi Zhong, Zhiguo Zhang\*, Zhengyu Ma\*  <br>
  **_已被 AAAI 2026 Main Track 接收！_**  
  **Code:** [Link](https://github.com/JackieWang9811/SCommander)

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">NeurIPS 2025</span> [
S&sup2;M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection](https://arxiv.org/abs/2508.05164),
   <ins>**Jiaqi Wang**</ins>, Zhengyu Ma\*, Xiongri Shen, Chenlin Zhou, Leilei Zhao, Han Zhang, Yi Zhong, Siqi Cai, Zhenxi Song, Zhiguo Zhang\* <br>
  **_ArXiv 2025.08  ➡️ 已被 NeurIPS 2025 Main Track 接收！_**  
  **Code:** [Link](https://github.com/JackieWang9811/S2M-Former) 

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">Neural Networks</span> [Efficient Speech Command Recognition Leveraging Spiking Neural Network and Curriculum Learning-based Knowledge Distillation](https://arxiv.org/abs/2412.12858),
   <ins>**Jiaqi Wang**</ins>,  Liutao Yu, Liwei Huang, Chenlin Zhou, Han Zhang, Zhenxi Song, Min Zhang, Zhengyu Ma\*, Zhiguo Zhang\* <br>
  **_ArXiv 2024.12  ➡️ 已被 Neural Networks 接收（2025.10）！_**  
  **Code:** [Link](https://github.com/JackieWang9811/SpikeSCR) 

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">ACL 2024</span> [Enhancing EEG-to-Text Decoding through Transferable Representations from Pre-trained Contrastive EEG-Text Masked Autoencoder](https://arxiv.org/abs/2402.17433),
   <ins>**Jiaqi Wang**</ins>,  Zhenxi Song\*,  Zhengyu Ma, Xipeng Qiu, Min Zhang, Zhiguo Zhang\* <br>
  **_ArXiv 2024.02 ➡️ 已被 ACL 2024 Main Conference 接收！_**  
  **Code:** [Link](https://github.com/JackieWang9811/CET-MAE) 
    
- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">Biomedical Signal Processing and Control</span> [A multi-classification algorithm based on multi-domain information fusion for motor imagery BCI](https://www.sciencedirect.com/science/article/pii/S1746809422007066),
  <ins>**Jiaqi Wang**</ins>, Wanzhong Chen, Mingyang Li\* <br>
  **_Biomedical Signal Processing and Control (BSPC) 2023.01_**

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">CN Invention Patent</span> [A human-like robot motion system and control method based on human body posture control](https://kns.cnki.net/kcms2/article/abstract?v=kxaUMs6x7-4I2jr5WTdXti3zQ9F92xu0nlgSAA876Br4k7Yiof5ge6un4lKDiSbV1SxF4BaaQuhTiBmtvRHVjHSjjN-2-bNX&uniplatform=NZKPT), <ins>**Jiaqi Wang**</ins>, Wanzhong Chen, Xiao Zheng<br>
  **_中国发明专利授权，2022.08_**

📖 **合作论文**

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">AAAI 2026 Oral</span> [Spikingformer: A Key Foundation Model for Spiking Neural Networks](https://openreview.net/forum?id=SmZTeHYlCa&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DAAAI.org%2F2026%2FConference%2FAuthors%23your-submissions)),
 Chenlin Zhou, Liutao Yu, Zhaokun Zhou, Han Zhang, <ins>**Jiaqi Wang**</ins>, Zhengyu Ma, Huihui Zhou, Yonghong Tian

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">ArXiv</span> [Temporal-adaptive Weight Quantization for Spiking Neural Networks](https://arxiv.org/abs/2511.17567),
 Han Zhang, Qingyan Meng, <ins>**Jiaqi Wang**</ins>, Baiyu Chen, Zhengyu Ma, Xiaopeng Fan

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">Information Fusion 2026</span> [BrainCSD: A Hierarchical Consistency-Driven MoE Foundation Model for Unified Connectome Synthesis and Multitask Brain Trait Prediction](https://arxiv.org/abs/2511.05630),
 Xiongri Shen, <ins>**Jiaqi Wang**</ins>, Yi Zhong, Zhenxi Song, Leilei Zhao, Liling Li, Yichen Wei, Lingyan Liang, Shuqiang Wang, Baiying Lei, Demao Deng, Zhiguo Zhang

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">Information Fusion 2026</span> [Pattern-Aware Diffusion Synthesis of fMRI/dMRI with Tissue and Microstructural Refinement](https://arxiv.org/abs/2511.04963),
 Xiongri Shen, <ins>**Jiaqi Wang**</ins>, Yi Zhong, Zhenxi Song, Leilei Zhao, Yichen Wei, Lingyan Liang, Shuqiang Wang, Baiying Lei, Demao Deng, Zhiguo Zhang

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">ACL 2025 Findings</span> [BrainECHO: Semantic Brain Signal Decoding through Vector-Quantized Spectrogram Reconstruction for Whisper-Enhanced Text Generation](https://arxiv.org/abs/2410.14971),
 Jilong Li, Zhenxi Song, <ins>**Jiaqi Wang**</ins>, Meishan Zhang, Honghai Liu, Min Zhang, Zhiguo Zhang

- <span style="display:inline-block; background-color:#00369F; color:#fff; padding:0px 7px; margin-right:5px; font-size:13px;">MICCAI 2025</span> [Thread the Needle: Genomics-Guided Prompt-Bridged Attention Model for Survival Prediction of Glioma Based on MRI Images](https://arxiv.org/abs/2410.14971),
Yi Zhong, Xubin Zheng, Xiongri Shen, <ins>**Jiaqi Wang**</ins>, Leilei Zhao, Zhenxi Song, Zhiguo Zhang


## 🎓 教育经历
{: #education .section-title }

<div class="edu-container">

  <div class="edu-item">
    <div class="edu-left">
      <img src="../images/logo_hitsz.png" class="edu-logo" alt="HITSZ logo">
      <img src="../images/logo_pcl.png" class="edu-logo" alt="PCL logo">
    </div>
    <div class="edu-text">
      <strong>哈尔滨工业大学（深圳）& 鹏城实验室</strong>  
      <br> 计算机科学与技术博士研究生（联合培养）  
      <br> 2023 至今
    </div>
  </div>

  <div class="edu-item">
    <div class="edu-left">
      <img src="../images/logo_jlu.png" class="edu-logo" alt="JLU logo">
    </div>
    <div class="edu-text">
      <strong>吉林大学</strong>  
      <br> 控制科学与工程硕士  
      <br> 2020 至 2023
    </div>
  </div>

  <div class="edu-item">
    <div class="edu-left">
      <img src="../images/logo_neepu.png" class="edu-logo" alt="NEEPU logo">
    </div>
    <div class="edu-text">
      <strong>东北电力大学</strong>  
      <br> 自动化学士  
      <br> 2016 至 2020
    </div>
  </div>

</div>

## 📚 学术服务
{: #academic-service .section-title }

我曾担任多个高水平 AI 会议与期刊的审稿人，包括：

**会议：** AAAI 2027; NeurIPS 2026; AAAI 2026; ACL ARR 2026/25（全年）; ICLR 2026/25; ICME 2026/25; ACM MM 2026/24; ICASSP 2026/23。<br>
**期刊：** IEEE TCSVT; Neurocomputing; Neuromorphic Computing and Engineering; IEEE TNSRE; IEEE TIM; Biomedical Signal Processing and Control, et al.

## 🔭 开源项目
{: #open-source-projects .section-title }

🧠 [Awesome Spiking Neural Networks](https://github.com/zhouchenlin2096/Awesome-Spiking-Neural-Networks)（600+ stars）  
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/zhouchenlin2096/Awesome-Spiking-Neural-Networks)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**这是一个关于脉冲神经网络的论文列表，包含论文、代码与相关网站。**  

如果你拥有或发现尚未收录的 SNN 论文，欢迎通过 pull request 补充到该项目中。


## 🏢 工作经历
{: #work-experience .section-title }

- 近期持续参与产业界大规模 AI 系统与真实产品场景相关研究
- 2022.06 至 2022.08，华为 ICT（Optic Line）AI 工程师实习生，研究方向为 3D 计算机视觉与 FTTR


## ⭐ 奖励荣誉
{: #awards .section-title }

- 2026 受邀参加**小红书 REDstar 顶尖人才计划技术沙龙**
- 2026 受邀参加**淘宝/淘天 Star 计划**
- 2023 奇安信公益奖学金，吉林大学仅 4 人获奖
- 2023 吉林大学优秀硕士毕业生，Top 6%
- 2022 研究生国家奖学金，Top 6%
- 2022 吉林大学优秀研究生二等奖
- 2021 吉林大学优秀研究生二等奖
- 2021 吉林大学优秀研究生，Top 4%
- 2021 “华为杯”第十八届中国研究生数学建模竞赛三等奖
- 2021 吉林大学研究生学业奖学金
- 2020 吉林大学研究生学业奖学金
- 2020 东北电力大学优秀毕业生
- 2019 东北电力大学优秀学生一等奖学金
- 2019 东北电力大学优秀学生

这些学术与产业经历让我持续连接前沿研究、真实场景与技术创新。


## 📸 高光时刻
{: #highlights .section-title }

这里记录了我科研旅程中的一些片段：

<div class="gallery">
  <img src="../images/AAAI2026_1.png" alt="AAAI 2026 highlight 1" class="gallery-image">
  <img src="../images/AAAI2026_2.png" alt="AAAI 2026 highlight 2" class="gallery-image">
  <img src="../images/Nips-poster.png" alt="NeurIPS poster" class="gallery-image">
  <img src="../images/page1.jpg" alt="Highlight 1" class="gallery-image">
  <img src="../images/page2.jpg" alt="Highlight 2" class="gallery-image">
  <img src="../images/page3.jpg" alt="Highlight 3" class="gallery-image">
  <img src="../images/page4.jpg" alt="Highlight 4" class="gallery-image">
  <img src="../images/techopenday-2026.jpg" alt="TechOPENDAY 高光时刻" class="gallery-image">
  <img src="../images/redstar-2026.jpg" alt="REDstar 技术沙龙高光时刻" class="gallery-image">
</div>


<style>
body, .page__content {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               "Helvetica Neue", Arial, sans-serif;
  font-size: 17px;
  line-height: 1.7;
}

.section-title {
  font-size: 20px;
  font-weight: 600;
  margin-top: 32px;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
}

.section-title::after {
  content: "";
  flex: 1;
  margin-left: 12px;
  border-bottom: 1px solid #e6e6e6;
}

.page__content > .section-title:first-of-type {
  margin-top: 10px;
}

.page__content ul {
  margin-top: 4px;
  margin-bottom: 8px;
}

.edu-container {
  display: flex;
  flex-direction: column;
  gap: 18px;
  margin-top: 10px;
}

.edu-item {
  display: flex;
  align-items: center;
  gap: 16px;
}

.edu-left {
  width: 140px;
  display: flex;
  gap: 10px;
  justify-content: flex-start;
}

.edu-logo {
  width: 55px;
  height: 55px;
  object-fit: contain;
}

.edu-text {
  font-size: 17px;
  line-height: 1.4;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin: 12px 0 26px;
}

.project-card {
  border: 1px solid #e6e9ef;
  border-radius: 8px;
  padding: 14px 15px;
  background: #ffffff;
  box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
}

.project-card__top,
.project-card__links,
.project-card__tags {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.project-card__top {
  justify-content: space-between;
  margin-bottom: 8px;
}

.project-card h3 {
  margin: 0 0 6px;
  font-size: 18px;
  line-height: 1.25;
}

.project-card p {
  min-height: 58px;
  margin: 0 0 10px;
  font-size: 14px;
  line-height: 1.45;
}

.project-card__venue,
.project-card__stars,
.project-card__tags span {
  display: inline-flex;
  align-items: center;
  min-height: 24px;
  border-radius: 6px;
  padding: 1px 8px;
  font-size: 12px;
  line-height: 1.2;
}

.project-card__venue {
  color: #ffffff;
  background: #00369F;
}

.project-card__stars {
  color: #314155;
  background: #f3f6fa;
}

.project-card__tags {
  margin-bottom: 12px;
}

.project-card__tags span {
  color: #4c5b6d;
  background: #f7f9fb;
  border: 1px solid #e7ebf0;
}

.project-card__links a {
  display: inline-flex;
  align-items: center;
  min-height: 28px;
  border: 1px solid #00369F;
  border-radius: 6px;
  padding: 2px 10px;
  color: #00369F;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
}

.project-card__links a:hover {
  color: #ffffff;
  background: #00369F;
}

@media (max-width: 760px) {
  .project-grid {
    grid-template-columns: 1fr;
  }

  .project-card p {
    min-height: 0;
  }
}

.gallery {
  display: flex;
  overflow-x: auto;
  gap: 20px;
  padding: 10px 0;
}

.gallery-image {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  flex-shrink: 0;
}

.language-switch {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 8px;
  margin-bottom: 18px;
  font-size: 14px;
}

.language-switch span,
.language-switch a {
  display: inline-flex;
  align-items: center;
  min-height: 30px;
  padding: 2px 10px;
  border: 1px solid #d6d6d6;
  border-radius: 6px;
  text-decoration: none;
}

.language-switch span {
  color: #ffffff;
  background: #00369F;
  border-color: #00369F;
}

.language-switch a {
  color: #00369F;
  background: #ffffff;
}

#about-me.anchor-target {
  display: block;
  height: 0;
  margin-top: 0;
  scroll-margin-top: 80px;
}
</style>
