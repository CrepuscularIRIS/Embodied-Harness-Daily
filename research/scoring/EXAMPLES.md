# embodied-v3.1 输出示例

全部论文信息、定位和结果均为虚构，仅检验格式与算术，不能进入正式队列。领域卡 ID 引用本仓库真实卡片，实际评分需读取对应卡及论文。

```json
{"paper_id":"SYNTH-EXAMPLE","version":"example","source_url":"https://example.invalid/paper","material_level":"core","status":"scored","claim_type":"component_training","move":"描述教师到学生的监督，信息可辨识性和匹配对照仍有限","gap":"虚构示例：已有方法在相关领域条件下存在具体失败。","patterns":{"primary":"embodied:privileged_teacher_supervision","subcards":[],"supporting":[],"status":"matched","reason":"论文操作与本领域卡的核心机制一致；这不是加分理由。"},"card_checks":[{"card":"embodied:privileged_teacher_supervision","criterion_ref":"patterns/main/privileged_teacher_supervision.md / Success conditions and Failure modes","criterion":"教师特权与学生可见信息的区分","verdict":"partial","paper_evidence":"虚构示例 §3 / Table 1 仅提供部分支持。","axes":["X","E"]}],"ratings":{"G":3,"M":3,"X":2,"E":2},"screen_score":58.75,"reasons":{"G":"示例 §2 指出具体问题，但相邻方法差别仍有限。","M":"示例 §3 的操作对准所述问题。","X":"相关领域卡要求的关键条件只得到部分说明（示例 §3）。","E":"相关领域卡要求的对照仍不充分（示例 Table 1）。"},"evidence":[{"locator":"虚构示例 §3 / Table 1","fact":"仅用来展示字段，非真实实验结果。"}],"claim_support":"scoped","evidence_level":"offline","caveat":"作者宣称更广范围，虚构材料只支持较窄结论。","needs":[]}
```

缺材料时：无法判断的轴和总分为 null，status=needs_material；不以零分或重算分母代替。无适用领域卡可记 unassigned，不回退到原 15＋31 分类。
