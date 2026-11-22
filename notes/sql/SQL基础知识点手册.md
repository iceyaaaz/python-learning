# SQL基础知识点手册（MySQL）

适用于数据分析方向的入门与刷题。下文示例表：employees(id, name, dept\_id, salary, hire\_date)，departments(id, dept\_name)，orders(order\_id, user\_id, amount, order\_date)。

## 目录（点击跳转）

**按需求快速查：** 刚入门看第一部分 1–12 节　|　查函数看 G、H、I 节　|　刷题模板看 R 节　|　易错点看 U 节　|　正则看 V 节　|　建表、增删改看 W 节

**第一部分：基础知识点**

- [1. 查询基础](#m22s1cf5rb4.162)
- [2. 条件筛选](#m22s1cf5rb4.543)
- [3. 聚合与分组](#m22s1cf5rb4.728)
- [4. 条件表达式 CASE WHEN](#m22s1cf5rb4.1086)
- [5. 多表连接](#m22s1cf5rb4.1336)
- [6. 子查询与 CTE](#m22s1cf5rb4.1782)
- [7. 窗口函数（MySQL 8.0+）](#m22s1cf5rb4.2208)
- [8. 常用函数](#m22s1cf5rb4.2632)
- [9. 增删改与建表](#m22s1cf5rb4.2880)
- [10. 高频题型模板](#m22s1cf5rb4.3415)
- [11. 常见易错点](#m22s1cf5rb4.3735)
- [12. 刷题方法](#m22s1cf5rb4.3963)

**[第二部分：全面对照查询手册（带使用频率）](#m22s1cf5rb4.4075)**

- [ ] [A. 查询与过滤](#m22s1cf5rb4.4171)
- [ ] [B. 聚合与分组](#m22s1cf5rb4.4724)
- [ ] [C. 连接与集合运算](#m22s1cf5rb4.5166)
- [ ] [D. 子查询与 CTE](#m22s1cf5rb4.5679)
- [ ] [E. 窗口函数（MySQL 8.0+）](#m22s1cf5rb4.5912)
- [ ] [F. 条件与空值处理](#m22s1cf5rb4.6530)
- [ ] [G. 字符串函数](#m22s1cf5rb4.6813)
- [ ] [H. 日期时间函数](#m22s1cf5rb4.7436)
- [ ] [I. 数值与类型转换](#m22s1cf5rb4.8048)
- [ ] [J. 常用数据类型](#m22s1cf5rb4.8428)
- [ ] [K. JSON 函数（低频）](#m22s1cf5rb4.8794)
- [ ] [L. 数据操作 DML](#m22s1cf5rb4.9067)
- [ ] [M. 表结构 DDL 与约束](#m22s1cf5rb4.9423)
- [ ] [N. 索引与性能优化](#m22s1cf5rb4.9941)
- [ ] [O. 事务与锁](#m22s1cf5rb4.10346)
- [ ] [P. 数据库设计](#m22s1cf5rb4.10602)
- [ ] [Q. 其他数据库对象](#m22s1cf5rb4.10828)
- [ ] [R. 数据分析高频业务模板](#m22s1cf5rb4.10986)
- [ ] [S. MySQL 与 Hive/Spark SQL 常见差异](#m22s1cf5rb4.12551)
- [ ] [T. 学习优先级建议](#m22s1cf5rb4.13184)
- [ ] [U. 易忽略的小知识点与常见陷阱](#m22s1cf5rb4.13532)
  - [U1. 空值（NULL）相关](#m22s1cf5rb4.13627)
  - [U2. 连接与重复数据](#m22s1cf5rb4.14179)
  - [U3. 类型、日期与计算](#m22s1cf5rb4.14548)
  - [U4. 分组、排序与分页](#m22s1cf5rb4.15142)
  - [U5. 窗口函数](#m22s1cf5rb4.15646)
  - [U6. 写操作与数据库对象](#m22s1cf5rb4.15949)
  - [U7. 检查清单](#m22s1cf5rb4.16335)
- [ ] [V. 正则表达式（REGEXP）常用符号速查](#m22s1cf5rb4.16599)
  - [V1. 基本用法](#m22s1cf5rb4.16682)
  - [V2. 位置符号](#m22s1cf5rb4.17281)
  - [V3. 单个字符的写法](#m22s1cf5rb4.17364)
  - [V4. 重复次数](#m22s1cf5rb4.17762)
  - [V5. 分组与或](#m22s1cf5rb4.17972)
  - [V6. 常用模板](#m22s1cf5rb4.18176)
  - [V7. 以 SQL40 为例的完整分析](#m22s1cf5rb4.18609)
  - [V8. 易错点](#m22s1cf5rb4.19004)
  - [V9. 不同数据库的写法](#m22s1cf5rb4.19482)
  - [V10. 学习建议](#m22s1cf5rb4.19743)
- [ ] [W. 建表与增删改实操指南（带完整示例）](#m22s1cf5rb4.19900)
  - [ ] [W1. 语句分类](#m22s1cf5rb4.19998)
  - [ ] [W2. 先认识环境：库与表](#m22s1cf5rb4.20272)
  - [ ] [W3. 建表 CREATE TABLE](#m22s1cf5rb4.20596)
  - [ ] [W4. 插入数据 INSERT](#m22s1cf5rb4.21638)

* [ ] [W5. 修改数据 UPDATE](#m22s1cf5rb4.22558)

- [ ] [W6. 删除数据 DELETE](#m22s1cf5rb4.23256)
- [ ] [W7. 清空与删表：三者对比](#m22s1cf5rb4.23543)
- [ ] [W8. 修改表结构 ALTER TABLE](#m22s1cf5rb4.23821)
- [ ] [W9. 用事务给自己加保险](#m22s1cf5rb4.24583)
- [ ] [W10. 常用实用写法](#m22s1cf5rb4.24994)
- [ ] [W11. 常见报错与处理](#m22s1cf5rb4.25364)
- [ ] [W12. 执行前的检查清单](#m22s1cf5rb4.26096)
- [ ] [W13. 动手练习任务](#m22s1cf5rb4.26284)

## 1. 查询基础

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
SELECT DISTINCT name, salary AS 工资
FROM employees
WHERE salary > 8000
ORDER BY salary DESC
LIMIT 10;
```

- DISTINCT：去重；AS：起别名；ORDER BY 默认升序 ASC，降序用 DESC。
- LIMIT n OFFSET m：跳过 m 行后取 n 行。

**书写顺序与执行顺序不同（重点）**

- 书写：SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
- 执行：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
- 所以 WHERE 里不能使用 SELECT 中定义的别名，ORDER BY 里可以。

## 2. 条件筛选

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

- 比较：=、<>（不等于）、>、<、>=、<=
- 范围：BETWEEN a AND b（包含两端）；集合：IN (1, 2, 3)
- 模糊：LIKE '张%'（以张开头）、'%a'（以a结尾）、'\_a%'（第二个字符是a）
- 空值：只能用 IS NULL / IS NOT NULL，不能写 = NULL
- AND 优先级高于 OR，混用时务必加括号

## 3. 聚合与分组

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
SELECT dept_id, COUNT(*) AS cnt, AVG(salary) AS avg_sal
FROM employees
WHERE hire_date >= '2024-01-01'
GROUP BY dept_id
HAVING COUNT(*) >= 3
ORDER BY avg_sal DESC;
```

- 常用聚合函数：COUNT、SUM、AVG、MAX、MIN。
- COUNT(\*) 统计所有行；COUNT(列) 不统计 NULL；COUNT(DISTINCT 列) 统计不重复值。
- **WHERE 与 HAVING 的区别**：WHERE 在分组前过滤行，HAVING 在分组后过滤组，可以使用聚合函数。
- SELECT 中出现的非聚合列，必须写在 GROUP BY 里。

## 4. 条件表达式 CASE WHEN

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
SELECT name,
  CASE WHEN salary >= 15000 THEN '高'
       WHEN salary >= 8000 THEN '中'
       ELSE '低' END AS level
FROM employees;
```

条件计数/占比的常用写法：

```sql
SELECT SUM(CASE WHEN amount > 100 THEN 1 ELSE 0 END) / COUNT(*) AS ratio
FROM orders;
```

## 5. 多表连接

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

- INNER JOIN：只保留两表都匹配的行。
- LEFT JOIN：保留左表全部行，右表无匹配则为 NULL。RIGHT JOIN 同理反过来。
- MySQL 不支持 FULL JOIN，可用 LEFT JOIN UNION RIGHT JOIN 实现。
- ON 写连接条件；LEFT JOIN 后若把右表条件写进 WHERE，会把 NULL 行过滤掉，效果变成 INNER JOIN。右表的过滤条件通常写在 ON 里。
- 找左表中没有匹配的行：LEFT JOIN 后加 WHERE 右表.id IS NULL。
- 自连接：同一张表起两个别名相互连接，常用于找上下级、比较相邻记录。
- UNION 合并结果并去重，UNION ALL 合并不去重（更快，优先使用）。两段查询的列数和类型要一致。

## 6. 子查询与 CTE

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
-- 子查询：高于平均工资的员工
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- CTE：用 WITH 把中间结果命名，逻辑更清晰
WITH dept_avg AS (
  SELECT dept_id, AVG(salary) AS avg_sal
  FROM employees GROUP BY dept_id
)
SELECT e.name, e.salary, d.avg_sal
FROM employees e JOIN dept_avg d ON e.dept_id = d.dept_id
WHERE e.salary > d.avg_sal;
```

- IN / NOT IN / EXISTS 常与子查询搭配。NOT IN 遇到子查询结果含 NULL 会出错，可改用 NOT EXISTS。

## 7. 窗口函数（MySQL 8.0+）

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

基本形式：函数() OVER (PARTITION BY 分组列 ORDER BY 排序列)

- 排名：ROW\_NUMBER()（不重复）、RANK()（并列后跳号，如 1,1,3）、DENSE\_RANK()（并列不跳号，如 1,1,2）
- 聚合：SUM() OVER、AVG() OVER，用于累计、占比
- 前后取值：LAG(列, n)（取前 n 行）、LEAD(列, n)（取后 n 行）

```sql
-- 每个部门工资前2名
SELECT * FROM (
  SELECT name, dept_id, salary,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rk
  FROM employees
) t
WHERE rk <= 2;
```

窗口函数不能直接写在 WHERE 里，需要套一层子查询或 CTE 再过滤。

## 8. 常用函数

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

- 字符串：CONCAT、SUBSTRING、LENGTH、REPLACE、TRIM、UPPER、LOWER
- 日期：NOW()、CURDATE()、DATE\_FORMAT(d, '%Y-%m')、DATEDIFF(a, b)、DATE\_ADD(d, INTERVAL 1 DAY)、YEAR()、MONTH()
- 数值：ROUND、FLOOR、CEIL、ABS
- 空值处理：IFNULL(a, b)、COALESCE(a, b, c)（取第一个非空）、NULLIF(a, b)

## 9. 增删改与建表

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

```sql
INSERT INTO employees (name, dept_id, salary) VALUES ('张三', 1, 9000);
UPDATE employees SET salary = salary + 500 WHERE id = 1;
DELETE FROM employees WHERE id = 1;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  created_at DATETIME DEFAULT NOW()
);
```

- UPDATE 和 DELETE 必须带 WHERE，否则会影响整张表。
- 常见约束：PRIMARY KEY（主键）、NOT NULL、UNIQUE、DEFAULT、FOREIGN KEY（外键）。
- 分类：DDL（建/改/删表结构）、DML（增删改）、DQL（查询）、DCL（权限）。
- 事务：START TRANSACTION → COMMIT / ROLLBACK，保证一组操作要么全成功、要么全回滚。

## 10. 高频题型模板

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

- **找重复数据**：GROUP BY 列 HAVING COUNT(\*) > 1
- **分组 TopN**：窗口函数 ROW\_NUMBER/DENSE\_RANK 加 PARTITION BY，外层过滤 rk <= N
- **第二高的值**：DENSE\_RANK() = 2，或 LIMIT 1 OFFSET 1（注意不存在时应返回 NULL）
- **环比/同比**：LAG() 取上一期，再相减相除
- **累计值**：SUM() OVER (ORDER BY 日期)
- **留存/连续登录**：先去重，再用日期差或窗口函数构造分组
- **占比**：SUM(CASE WHEN ...) / COUNT(\*)，或 SUM(x) / SUM(SUM(x)) OVER ()

## 11. 常见易错点

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

1. 用 = NULL 判断空值，应写 IS NULL。
2. COUNT(列) 不计 NULL，和 COUNT(\*) 结果可能不同。
3. 整数相除在 MySQL 中会得到小数，注意用 ROUND 控制精度。
4. GROUP BY 漏写非聚合列。
5. LEFT JOIN 后把右表条件写进 WHERE，导致左表行丢失。
6. 日期比较时，BETWEEN 对 DATETIME 的结束日期可能漏掉当天的非零点数据。
7. 窗口函数直接写在 WHERE 里。

## 12. 刷题方法

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

1. 先自己写，卡住超过10分钟再看答案。
2. 看完后，用自己的话讲出每个关键词为什么这样写。
3. 做错的题记入错题本，写明错因，隔几天重做一遍。
4. 按类型集中练：先单表和聚合，再连接，再子查询，最后窗口函数。

# 第二部分：全面对照查询手册（带使用频率）

**频率说明：** ★★★ 高频必会　★★ 中频建议掌握　★ 低频了解即可，遇到再查。以 MySQL 8.0 为主，Hive/Spark 的差异见 S 节。

## A. 查询与过滤

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| SELECT … FROM | 取列、取表；少用 SELECT \* | ★★★ |
| WHERE | 行过滤：`WHERE age > 18 AND city = '北京'` | ★★★ |
| DISTINCT | 去重 | ★★★ |
| ORDER BY | 排序：`ORDER BY a DESC, b ASC` | ★★★ |
| LIMIT / OFFSET | 分页：`LIMIT 10 OFFSET 20` | ★★★ |
| AS 别名 | 列别名、表别名 | ★★★ |
| IN / NOT IN | 集合判断；NOT IN 遇到 NULL 会出错 | ★★★ |
| BETWEEN … AND | 闭区间，含两端 | ★★★ |
| LIKE | `%` 任意长度，`_` 单个字符 | ★★★ |
| IS NULL / IS NOT NULL | 判空，不能写 = NULL | ★★★ |
| EXISTS / NOT EXISTS | 存在性判断，常配合相关子查询 | ★★ |
| REGEXP / RLIKE | 正则匹配 | ★ |
| ANY / ALL / SOME | 与子查询结果逐个比较 | ★ |
| <=> | MySQL 空值安全的相等比较 | ★ |
| ORDER BY FIELD() | 按自定义顺序排序 | ★ |

## B. 聚合与分组

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| COUNT / SUM / AVG / MAX / MIN | 基础聚合；COUNT(列) 不计 NULL | ★★★ |
| COUNT(DISTINCT 列) | 去重计数（如 UV） | ★★★ |
| GROUP BY | 分组，可多列 | ★★★ |
| HAVING | 对分组结果过滤 | ★★★ |
| GROUP\_CONCAT | 把一组值拼成字符串（Hive 用 collect\_list + concat\_ws） | ★★ |
| 条件聚合 | `SUM(CASE WHEN … THEN 1 ELSE 0 END)`，统计分类数量、占比 | ★★★ |
| STDDEV / VARIANCE | 标准差、方差 | ★ |
| WITH ROLLUP | 分组后追加小计、总计行 | ★ |
| GROUPING SETS / CUBE | 多维度汇总（MySQL 不支持，Hive/Spark 支持） | ★ |
| BIT\_AND / BIT\_OR | 位运算聚合 | ★ |

## C. 连接与集合运算

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| INNER JOIN | 只保留两表都匹配的行 | ★★★ |
| LEFT JOIN | 保留左表全部行，右表无匹配为 NULL | ★★★ |
| RIGHT JOIN | 与 LEFT 相反，一般改写成 LEFT 使用 | ★★ |
| FULL OUTER JOIN | 两表全保留（MySQL 不支持，用 LEFT UNION RIGHT 模拟） | ★ |
| 自连接 | 同表别名连接，用于上下级、相邻记录比较 | ★★ |
| CROSS JOIN | 笛卡尔积，用于生成日期×类别等全组合 | ★ |
| ON 与 WHERE 的区别 | LEFT JOIN 时右表条件写 ON，写 WHERE 会变成 INNER | ★★★ |
| 多表连接 | 三表及以上，逐个 JOIN | ★★★ |
| UNION | 合并并去重 | ★★★ |
| UNION ALL | 合并不去重，更快 | ★★★ |
| INTERSECT / EXCEPT | 交集 / 差集（MySQL 8.0.31+ 才支持，常用 JOIN 或 EXISTS 代替） | ★ |
| NATURAL JOIN / USING | 按同名列连接的简写 | ★ |

## D. 子查询与 CTE

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| 标量子查询 | 返回单个值，用于比较或做列 | ★★★ |
| IN 子查询 | `WHERE id IN (SELECT …)` | ★★★ |
| 派生表 | FROM 中的子查询，必须起别名 | ★★★ |
| 相关子查询 | 子查询引用外层字段，逐行执行，性能较差 | ★★ |
| CTE（WITH … AS） | 给中间结果命名，逻辑清晰，笔试面试首选 | ★★★ |
| 递归 CTE | 处理层级、树形结构、生成连续日期 | ★ |

## E. 窗口函数（MySQL 8.0+）

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

基本形式：`函数() OVER (PARTITION BY 分组列 ORDER BY 排序列 [窗口帧])`

| 知识点 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| ROW\_NUMBER() | 连续编号，不并列 | ★★★ |
| RANK() | 并列后跳号（1,1,3） | ★★★ |
| DENSE\_RANK() | 并列不跳号（1,1,2） | ★★★ |
| LAG(列, n) / LEAD(列, n) | 取前 / 后第 n 行，用于环比、相邻比较 | ★★★ |
| SUM / AVG / COUNT OVER | 累计、占比、组内汇总 | ★★★ |
| 窗口帧 ROWS BETWEEN … | 移动平均：`ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` | ★★ |
| FIRST\_VALUE / LAST\_VALUE / NTH\_VALUE | 取窗口内首、尾、第 n 个值；LAST\_VALUE 需注意默认窗口帧 | ★★ |
| NTILE(n) | 平均分成 n 桶，用于分层 | ★ |
| PERCENT\_RANK / CUME\_DIST | 百分位排名 | ★ |
| RANGE 与 ROWS 的区别 | RANGE 按值范围，ROWS 按物理行数 | ★ |
| 命名窗口 WINDOW w AS (…) | 复用同一窗口定义 | ★ |

注意：窗口函数不能直接写在 WHERE 里，需套一层子查询或 CTE 再过滤。

## F. 条件与空值处理

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| CASE WHEN | 多条件分支，分层、行转列、条件聚合都靠它 | ★★★ |
| IF(条件, 真, 假) | MySQL 简写（Hive 也支持） | ★★ |
| IFNULL(a, b) | a 为空取 b（Hive 用 nvl） | ★★★ |
| COALESCE(a, b, c) | 取第一个非空值，通用写法 | ★★★ |
| NULLIF(a, b) | 两者相等返回 NULL，常用于避免除 0 | ★★ |
| NULL 的运算规则 | 任何值与 NULL 运算结果都是 NULL；聚合函数忽略 NULL | ★★★ |

## G. 字符串函数

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 函数 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| CONCAT(a, b, …) | 拼接；任一参数为 NULL 则结果为 NULL | ★★★ |
| CONCAT\_WS(分隔符, a, b) | 带分隔符拼接，忽略 NULL | ★★ |
| SUBSTRING / SUBSTR(s, 起始, 长度) | 截取，下标从 1 开始 | ★★★ |
| LEFT / RIGHT(s, n) | 取左 / 右 n 个字符 | ★★★ |
| LENGTH / CHAR\_LENGTH | 字节长度 / 字符长度（中文差别明显） | ★★ |
| UPPER / LOWER | 大小写转换 | ★★ |
| TRIM / LTRIM / RTRIM | 去空格 | ★★ |
| REPLACE(s, 旧, 新) | 替换 | ★★ |
| INSTR / LOCATE | 查找子串位置 | ★★ |
| SUBSTRING\_INDEX(s, 分隔符, n) | 按分隔符取前 / 后 n 段，拆字符串常用 | ★★ |
| LPAD / RPAD | 左 / 右补齐 | ★ |
| REVERSE | 反转字符串 | ★ |
| FORMAT(数, 小数位) | 千分位格式化 | ★ |
| FIND\_IN\_SET(x, 'a,b,c') | 在逗号分隔串中找位置 | ★ |
| REGEXP\_REPLACE / REGEXP\_SUBSTR | 正则替换 / 提取（8.0+） | ★ |
| ASCII / CHAR | 字符与编码转换 | ★ |

## H. 日期时间函数

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 函数 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| NOW() / CURDATE() / CURRENT\_DATE | 当前时间 / 当前日期 | ★★★ |
| DATE\_FORMAT(d, '%Y-%m-%d') | 格式化；常用 `%Y-%m` 按月分组 | ★★★ |
| YEAR / MONTH / DAY / HOUR | 取年月日时 | ★★★ |
| DATE(datetime) | 取日期部分 | ★★★ |
| DATEDIFF(a, b) | 两日期相差天数 | ★★★ |
| DATE\_ADD / DATE\_SUB(d, INTERVAL n DAY) | 日期加减，单位可为 DAY、MONTH、YEAR | ★★★ |
| TIMESTAMPDIFF(单位, a, b) | 按指定单位求差（秒、分、天、月） | ★★ |
| LAST\_DAY(d) | 当月最后一天 | ★★ |
| STR\_TO\_DATE(s, 格式) | 字符串转日期 | ★★ |
| WEEK / WEEKDAY / DAYOFWEEK | 取第几周 / 星期几（三者起点不同，易错） | ★★ |
| UNIX\_TIMESTAMP / FROM\_UNIXTIME | 时间戳与日期互转 | ★★ |
| EXTRACT(YEAR FROM d) | 通用的取值写法 | ★ |
| DAYNAME / MONTHNAME | 星期、月份名称 | ★ |
| 生成连续日期 | 用递归 CTE 或日历表 | ★ |

## I. 数值与类型转换

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 函数 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| ROUND(x, n) | 四舍五入到 n 位 | ★★★ |
| CAST(x AS 类型) / CONVERT | 类型转换，如 `CAST(a AS DECIMAL(10,2))`、`AS SIGNED` | ★★★ |
| FLOOR / CEIL | 向下 / 向上取整 | ★★ |
| ABS | 绝对值 | ★★ |
| MOD(a, b) 或 a % b | 取余，判奇偶、分组 | ★★ |
| GREATEST / LEAST | 多个值取最大 / 最小 | ★★ |
| TRUNCATE(x, n) | 截断小数，不四舍五入 | ★ |
| POWER / SQRT / LOG | 幂、开方、对数 | ★ |
| RAND() | 随机数，可用于随机抽样 | ★ |
| 除法 | 整数相除在 MySQL 得小数，/ 与 DIV（整除）不同 | ★★ |

## J. 常用数据类型

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 类型 | 说明 | 频率 |
| --- | --- | --- |
| INT / BIGINT | 整数，ID 常用 BIGINT | ★★★ |
| DECIMAL(m, n) | 精确小数，金额必用 | ★★★ |
| FLOAT / DOUBLE | 近似小数，有精度误差 | ★★ |
| VARCHAR(n) | 可变长字符串 | ★★★ |
| CHAR(n) | 定长字符串，适合固定长度编码 | ★★ |
| TEXT | 长文本 | ★★ |
| DATE / DATETIME / TIMESTAMP | 日期 / 日期时间 / 时间戳（有时区与范围差异） | ★★★ |
| TINYINT(1) | MySQL 中常当布尔值使用 | ★★ |
| ENUM / SET | 枚举 / 集合类型 | ★ |
| JSON | 存 JSON 数据（8.0 支持） | ★ |
| BLOB | 二进制数据 | ★ |

## K. JSON 函数（低频）

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 函数 | 作用 | 频率 |
| --- | --- | --- |
| `列->'$.key'` / `列->>'$.key'` | 取 JSON 字段（->> 去引号） | ★ |
| JSON\_EXTRACT / JSON\_OBJECT / JSON\_ARRAY | 提取、构造 JSON | ★ |
| JSON\_CONTAINS / JSON\_SET | 判断包含、修改 | ★ |
| JSON\_TABLE | 把 JSON 数组展开成行 | ★ |

Hive/Spark 中日志数据常存 JSON，对应函数是 get\_json\_object、json\_tuple，互联网公司更常见。

## L. 数据操作 DML

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 示例 | 频率 |
| --- | --- | --- |
| INSERT INTO … VALUES | 插入，可一次插多行 | ★★★ |
| INSERT INTO … SELECT | 把查询结果插入另一张表 | ★★ |
| UPDATE … SET … WHERE | 修改；必须带 WHERE | ★★★ |
| DELETE FROM … WHERE | 删除行；必须带 WHERE | ★★★ |
| TRUNCATE TABLE | 清空表，不可回滚，比 DELETE 快 | ★★ |
| INSERT … ON DUPLICATE KEY UPDATE | 存在则更新，不存在则插入 | ★★ |
| REPLACE INTO | 先删后插，慎用 | ★ |
| 多表 UPDATE / DELETE | 配合 JOIN 修改或删除 | ★ |

## M. 表结构 DDL 与约束

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| CREATE DATABASE / TABLE | 建库、建表 | ★★★ |
| ALTER TABLE ADD / DROP / MODIFY / CHANGE | 加列、删列、改列类型、改列名 | ★★ |
| DROP TABLE / DATABASE | 删除，不可恢复 | ★★ |
| PRIMARY KEY | 主键，唯一且非空 | ★★★ |
| FOREIGN KEY | 外键，保证引用完整性 | ★★ |
| UNIQUE / NOT NULL / DEFAULT | 唯一、非空、默认值 | ★★★ |
| AUTO\_INCREMENT | 自增 | ★★★ |
| CHECK | 检查约束（8.0.16 起才生效） | ★ |
| COMMENT | 表、列注释 | ★★ |
| CREATE VIEW | 视图，封装复杂查询 | ★★ |
| 临时表 CREATE TEMPORARY TABLE | 会话内存放中间结果 | ★ |
| 约束与级联（ON DELETE CASCADE） | 外键删除时的联动规则 | ★ |
| SQL 分类 DDL / DML / DQL / DCL / TCL | 面试常考概念 | ★★ |

## N. 索引与性能优化

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| 索引作用与代价 | 加快查询，但减慢写入、占空间 | ★★ |
| 主键索引 / 唯一索引 / 普通索引 | 基本类型 | ★★ |
| 联合索引与最左前缀 | 按最左列顺序才能用上 | ★★ |
| B+ 树结构 | InnoDB 默认索引结构，面试常问 | ★★ |
| 覆盖索引、回表 | 查询列都在索引里就不用回表 | ★ |
| EXPLAIN | 查看执行计划（type、key、rows） | ★★ |
| 索引失效场景 | 对列用函数或运算、隐式类型转换、LIKE '%x'、前导 OR、<> 等 | ★★ |
| 全文索引、哈希索引 | 特定场景 | ★ |
| 慢查询日志 | 定位慢 SQL | ★ |
| 分区表、分库分表 | 大数据量方案，偏开发 | ★ |
| 写法优化 | 少用 SELECT \*、避免在 WHERE 里对列做函数、用 UNION ALL 代替 UNION、先过滤再连接 | ★★ |

## O. 事务与锁

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| ACID | 原子性、一致性、隔离性、持久性 | ★★ |
| START TRANSACTION / COMMIT / ROLLBACK | 事务控制 | ★★ |
| 四种隔离级别 | 读未提交、读已提交、可重复读（MySQL 默认）、串行化 | ★★ |
| 脏读、不可重复读、幻读 | 并发带来的三类问题 | ★★ |
| MVCC、行锁、表锁、间隙锁 | InnoDB 并发机制，偏开发面试 | ★ |
| 死锁 | 成因与排查 | ★ |
| SAVEPOINT | 事务内的保存点 | ★ |

## P. 数据库设计

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 作用 / 说明 | 频率 |
| --- | --- | --- |
| 一对一、一对多、多对多 | 表关系，多对多需中间表 | ★★ |
| 三大范式 1NF / 2NF / 3NF | 减少冗余的设计规则，面试常问 | ★★ |
| 主键设计 | 自增 ID、业务主键、UUID 的取舍 | ★ |
| 事实表与维度表 | 数据分析、数仓的基础概念 | ★★ |
| 星型 / 雪花模型 | 数仓建模方式 | ★ |
| 数据仓库分层（ODS、DWD、DWS、ADS） | 互联网公司数据岗常见 | ★ |

## Q. 其他数据库对象（偏开发，分析岗低频）

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 知识点 | 说明 | 频率 |
| --- | --- | --- |
| 存储过程 / 自定义函数 | 封装逻辑反复调用 | ★ |
| 触发器 | 增删改时自动执行 | ★ |
| 游标 | 逐行处理结果集 | ★ |
| GRANT / REVOKE | 授权与回收权限 | ★ |
| 备份与恢复（mysqldump） | 运维相关 | ★ |

## R. 数据分析高频业务模板

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

这一节比单个语法点更重要，面试和笔试多数是这类题。

**1. 分组 TopN（★★★）**

```sql
SELECT * FROM (
  SELECT dept_id, name, salary,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rk
  FROM employees
) t WHERE rk <= 3;
```

**2. 找重复数据（★★★）**

```sql
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id HAVING COUNT(*) > 1;
```

**3. 次日留存率（★★★）**

```sql
SELECT a.dt,
       COUNT(DISTINCT a.user_id) AS new_users,
       COUNT(DISTINCT b.user_id) AS retained,
       COUNT(DISTINCT b.user_id) / COUNT(DISTINCT a.user_id) AS rate
FROM login a
LEFT JOIN login b
  ON a.user_id = b.user_id AND b.dt = DATE_ADD(a.dt, INTERVAL 1 DAY)
GROUP BY a.dt;
```

**4. 连续登录天数（★★★）**：先对每个用户的登录日期去重，用日期减去 ROW\_NUMBER 得到分组标识，同组即连续。

```sql
SELECT user_id, COUNT(*) AS days FROM (
  SELECT user_id, dt,
    DATE_SUB(dt, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY dt) DAY) AS grp
  FROM (SELECT DISTINCT user_id, dt FROM login) x
) y GROUP BY user_id, grp;
```

**5. 环比 / 同比（★★★）**

```sql
SELECT m, amount,
  amount / LAG(amount) OVER (ORDER BY m) - 1 AS mom
FROM monthly_sales;
```

**6. 累计与累计占比（★★★）**

```sql
SELECT dt, amount,
  SUM(amount) OVER (ORDER BY dt) AS cum,
  SUM(amount) OVER (ORDER BY dt) / SUM(amount) OVER () AS cum_ratio
FROM daily_sales;
```

**7. 行转列（★★）**

```sql
SELECT user_id,
  SUM(CASE WHEN subject = '数学' THEN score END) AS math,
  SUM(CASE WHEN subject = '语文' THEN score END) AS chinese
FROM scores GROUP BY user_id;
```

**8. 漏斗转化（★★）**：对每个环节分别 COUNT(DISTINCT user\_id)，再用后一步除以前一步。

**9. 用户分层 / RFM（★★）**：用 CASE WHEN 或 NTILE 按最近一次消费、频次、金额分档。

**10. 会话切分（★）**：用 LAG 计算相邻事件间隔，超过阈值就标记为新会话，再对标记做累计求和得到会话编号。

**11. 中位数（★）**：用 ROW\_NUMBER 与 COUNT 窗口取中间一行或两行平均（MySQL 无内置 MEDIAN）。

## S. MySQL 与 Hive/Spark SQL 常见差异

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

| 场景 | MySQL | Hive / Spark SQL |
| --- | --- | --- |
| 空值替换 | IFNULL | nvl 或 coalesce |
| 字符串合并分组 | GROUP\_CONCAT | concat\_ws(',', collect\_list(列)) |
| 日期格式化 | DATE\_FORMAT(d, '%Y-%m') | date\_format(d, 'yyyy-MM') |
| 日期加减 | DATE\_ADD(d, INTERVAL 1 DAY) | date\_add(d, 1) |
| 日期差 | DATEDIFF(a, b) | datediff(a, b) |
| 时间戳 | UNIX\_TIMESTAMP | unix\_timestamp / from\_unixtime |
| 展开数组为多行 | 无直接对应（用 JSON\_TABLE） | LATERAL VIEW explode(列) |
| 去重聚合 | COUNT(DISTINCT) | 同，也可用 collect\_set |
| FULL JOIN | 不支持 | 支持 |
| 多维汇总 | 仅 WITH ROLLUP | GROUPING SETS / CUBE |
| 分区 | PARTITION（偏运维） | 分区表是核心，WHERE 里必须带分区字段 |
| 引号 | 字符串单引号，标识符反引号 | 字符串单引号，标识符反引号 |
| 大小写 | 关键字不区分，表名在 Linux 下区分 | 关键字不区分 |

## T. 学习优先级建议

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

1. **第一优先（★★★ 全部）：** 查询过滤、聚合分组、CASE WHEN、LEFT/INNER JOIN、UNION ALL、子查询与 CTE、排名与 LAG/LEAD、基础字符串和日期函数、增删改与建表。
2. **第二优先（★★）：** 窗口帧、GROUP\_CONCAT、EXISTS、自连接、更多日期函数、索引与 EXPLAIN 基本原理、事务与隔离级别、范式。
3. **第三优先（★）：** 递归 CTE、JSON、正则、存储过程、触发器、分库分表、全文索引。遇到再查，不用提前学。
4. **目标岗位相关：** 数据分析岗优先把第二部分 R 节的模板题练熟；若面向互联网公司，再补 Hive/Spark 差异（S 节）。
5. **检验标准：** 对 ★★★ 的每一项，能不看资料写出示例并讲清原理，才算掌握。

## U. 易忽略的小知识点与常见陷阱

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

这一节收录刷题和面试中反复出现的「小坑」。建议每做完一道题，对照检查：连接后行数有没有被放大？NULL 会不会影响结果？日期、并列、空表这些边界怎么处理？

### U1. 空值（NULL）相关

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| NOT IN 遇到 NULL | 子查询结果只要含一个 NULL，`NOT IN` 就查不出任何行。改用 `NOT EXISTS`，或在子查询里加 `WHERE 列 IS NOT NULL` | ★★★ |
| `<>` 会排除 NULL | `WHERE col <> 'a'` 不包含 col 为 NULL 的行；要保留需写 `col <> 'a' OR col IS NULL` | ★★★ |
| NULL 参与运算 | `1 + NULL`、`CONCAT('a', NULL)` 都得 NULL，用 `IFNULL` 或 `COALESCE` 兜底 | ★★★ |
| 聚合遇到 NULL 或无数据 | SUM 返回 NULL，COUNT 返回 0；AVG 会忽略 NULL，要按 0 算需 `AVG(IFNULL(x, 0))` | ★★★ |
| GROUP BY / DISTINCT 与 NULL | 多个 NULL 被视为同一组，但 `NULL = NULL` 的比较结果不是真 | ★★ |
| 排序中的 NULL | MySQL 把 NULL 视为最小，升序排最前；其他数据库默认可能不同 | ★★ |
| CASE WHEN 缺少 ELSE | 不匹配的行返回 NULL，容易导致后续计算出错 | ★★ |

### U2. 连接与重复数据

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| 一对多连接放大数据 | 订单表连明细表后再对订单金额求和，同一订单金额会被重复累加。先聚合再连接，或确认连接键唯一 | ★★★ |
| LEFT JOIN 的条件位置 | 右表条件写在 WHERE 里，会把 NULL 行过滤掉，LEFT 变成 INNER；应放在 ON 里 | ★★★ |
| 多对多连接行数暴增 | 连接前先检查两边连接键是否唯一，必要时先去重或聚合 | ★★★ |
| UNION 与 UNION ALL | UNION 会去重，需要额外开销，不要在不需要去重时使用；列名取自第一个查询，末尾的 ORDER BY 作用于整个合并结果 | ★★ |
| DISTINCT 作用范围 | `SELECT DISTINCT a, b` 去重的是 (a, b) 的组合，不是只作用于第一列 | ★★ |

### U3. 类型、日期与计算

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| BETWEEN 与 DATETIME | `BETWEEN '2026-01-01' AND '2026-01-31'` 的右端是 1 月 31 日零点，当天其他时刻的数据会漏掉。稳妥写法：`>= '2026-01-01' AND < '2026-02-01'` | ★★★ |
| 除法行为因库而异 | MySQL 的 `/` 得小数，`DIV` 才是整除；PostgreSQL、SQL Server 的整数除以整数得整数；Hive、Spark 的 `/` 得小数 | ★★ |
| 浮点数误差 | FLOAT / DOUBLE 有精度误差，不要直接做相等比较；金额用 DECIMAL | ★★ |
| 隐式类型转换 | 字符串列与数字比较时列会被转换，可能让索引失效；字符串 `'10' < '9'` 按字符比较，结果为真 | ★★ |
| TIMESTAMP 与 DATETIME | 前者与时区相关、范围较小，后者原样存储 | ★ |
| 星期与周函数的起点 | `WEEK()` 默认周日为一周开始，`WEEKDAY()` 周一为 0，`DAYOFWEEK()` 周日为 1；`DATEDIFF(a, b)` 是 a 减 b | ★★ |
| 大小写与字符长度 | 字符串比较是否区分大小写取决于排序规则，MySQL 默认通常不区分；`LENGTH` 返回字节数，中文用 `CHAR_LENGTH` | ★★ |

### U4. 分组、排序与分页

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| 用 GROUP BY 取最高值对应的人 | `SELECT name, MAX(salary)` 在开启 ONLY\_FULL\_GROUP\_BY 时报错，旧环境里 name 是随机的一行。应使用窗口函数或子查询 | ★★★ |
| LIMIT 没有稳定排序 | 没有 ORDER BY 时顺序不确定；排序列有重复值时分页会重复或漏行，要加唯一列兜底排序 | ★★★ |
| 同一 SELECT 里引用别名 | `SELECT a + 1 AS x, x + 1` 会报错，后面的列不能直接用前面的别名 | ★★ |
| COUNT 的写法 | `COUNT(*)` 与 `COUNT(1)` 结果一致，都统计所有行；`COUNT(列)` 不计 NULL | ★★★ |
| WHERE 与 HAVING | 行级条件放 WHERE，聚合结果条件放 HAVING；HAVING 用 SELECT 别名是 MySQL 的非标准扩展，换库可能报错 | ★★★ |
| WHERE 中使用别名与窗口函数 | SELECT 的别名和窗口函数结果不能直接写进 WHERE，要用重复表达式、子查询或 CTE | ★★★ |

### U5. 窗口函数

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| ROW\_NUMBER 遇并列 | 排序值相同的行编号顺序不确定；要稳定，在 ORDER BY 里加唯一列 | ★★★ |
| 带 ORDER BY 的窗口默认帧 | 默认是从分区开头到当前行，并列值得到相同的累计值；`LAST_VALUE` 因此常取到当前行，需要显式写窗口帧 | ★★ |
| RANK 与 DENSE\_RANK | RANK 并列后跳号（1,1,3），DENSE\_RANK 不跳号（1,1,2）；求「第 N 高」通常用 DENSE\_RANK | ★★★ |
| 窗口函数不能嵌套在 WHERE | 需要先在子查询或 CTE 中算出，再在外层过滤 | ★★★ |

### U6. 写操作与数据库对象

| 陷阱 | 说明与正确写法 | 频率 |
| --- | --- | --- |
| UPDATE / DELETE 没有 WHERE | 会影响整张表。先用同样的条件写一遍 SELECT 核对行数，再执行；重要操作放进事务 | ★★★ |
| DELETE、TRUNCATE、DROP 的区别 | DELETE 逐行删除、可回滚；TRUNCATE 属于 DDL，通常不可回滚，会重置自增值；DROP 连表结构一起删除 | ★★ |
| 自动提交 | MySQL 默认每条语句自动提交，要事务保护需先 `START TRANSACTION` | ★★ |
| 引号与标识符 | 字符串用单引号；双引号在不同数据库里可能表示标识符；MySQL 的标识符用反引号 | ★★ |
| LIKE 的通配符与索引 | `%` 和 `_` 是通配符，查找字面量需转义；`LIKE 'abc%'` 能用到索引，`LIKE '%abc'` 通常不能 | ★★ |

### U7. 检查清单

每写完一条 SQL，按顺序过一遍：

1. **行数检查：** 连接前后行数是否符合预期，有没有被放大？
2. **NULL 检查：** 过滤、运算、聚合、比较里有没有受 NULL 影响的地方？
3. **边界检查：** 日期的起止、并列值、空表、除数为 0 如何处理？
4. **口径检查：** 统计的是行数、人数还是去重后的人数？时间范围是否一致？
5. **执行顺序检查：** 别名、聚合、窗口函数是否用在了不能用的位置？
6. **可移植性检查：** 用到了哪些 MySQL 独有的写法，换成 Hive 或其他数据库是否还能运行？
7. **验算：** 用一小批能手算的数据核对结果。

## V. 正则表达式（REGEXP）常用符号速查

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

正则表达式是用一串符号描述「字符串应该长什么样」的规则，常用于格式校验、提取和替换。本节以 MySQL 8.0 为主。

### V1. 基本用法

```sql
-- 符合规则的行保留
WHERE phone REGEXP '^[1-9][0-9]{9}$'
-- 不符合规则
WHERE phone NOT REGEXP '^[0-9]+$'
-- 等价的函数写法，可指定匹配选项
WHERE REGEXP_LIKE(phone, '^[0-9]+$')
```

| 用法 | 说明 | 频率 |
| --- | --- | --- |
| `列 REGEXP '规则'`（同义词 RLIKE） | 判断是否符合规则 | ★★★ |
| `NOT REGEXP` | 不符合规则 | ★★ |
| `REGEXP_LIKE(列, 规则, 选项)` | 函数写法（8.0+），选项如 `'c'` 区分大小写、`'i'` 不区分 | ★ |
| `REGEXP_SUBSTR(列, 规则)` | 提取第一个匹配的片段，如 `REGEXP_SUBSTR('abc123def', '[0-9]+')` 得 `123` | ★★ |
| `REGEXP_REPLACE(列, 规则, 替换)` | 把匹配的部分替换掉，如去掉所有数字 | ★★ |
| `REGEXP_INSTR(列, 规则)` | 返回第一个匹配的位置，从 1 开始，没有匹配返回 0 | ★ |

**和 LIKE 最大的区别：** LIKE 要求整个字符串符合模式，而 REGEXP 只要字符串里**包含**符合规则的片段就算匹配。所以做格式校验时，几乎都要加上开头 `^` 和结尾 `$`，否则一个很长的字符串里只要有一段合格，也会被放行。

### V2. 位置符号

| 符号 | 含义 | 频率 |
| --- | --- | --- |
| `^` | 字符串开头 | ★★★ |
| `$` | 字符串结尾 | ★★★ |
| `\\b` | 单词边界（8.0 中需写双反斜杠） | ★ |

### V3. 单个字符的写法

| 符号 | 含义 | 示例 | 频率 |
| --- | --- | --- | --- |
| `.` | 任意一个字符 | `a.c` 匹配 abc、a1c | ★★★ |
| `[abc]` | 方括号内的任意一个字符 | `[135]` 匹配 1、3 或 5 | ★★★ |
| `[a-z]` | 范围 | `[0-9]`、`[a-z]`、`[A-Za-z]` | ★★★ |
| `[^abc]` | 不在方括号内的任意一个字符（取反） | `[^0-9]` 匹配非数字 | ★★ |
| `\\d` | 数字，等价于 `[0-9]` | 需写双反斜杠 | ★★ |
| `\\w` | 字母、数字、下划线 | 需写双反斜杠 | ★ |
| `\\s` | 空白字符（空格、换行等） | 需写双反斜杠 | ★ |
| `[[:digit:]]` `[[:alpha:]]` `[[:alnum:]]` | POSIX 字符类，分别是数字、字母、字母和数字 | 可读性好 | ★ |
| `\\.` | 匹配真正的小数点，因为 `.` 本身是通配符 | 特殊符号要转义 | ★★★ |

### V4. 重复次数

| 符号 | 含义 | 示例 | 频率 |
| --- | --- | --- | --- |
| `*` | 0 次或多次 | `a*` | ★★ |
| `+` | 1 次或多次 | `[0-9]+` 表示一串数字 | ★★★ |
| `?` | 0 次或 1 次（可有可无） | `-?` 表示连字符可有可无 | ★★★ |
| `{n}` | 恰好 n 次 | `[0-9]{4}` | ★★★ |
| `{n,}` | 至少 n 次 | `[0-9]{6,}` | ★★ |
| `{n,m}` | n 到 m 次 | `[0-9]{3,5}` | ★★ |

### V5. 分组与或

| 符号 | 含义 | 频率 |
| --- | --- | --- |
| `( )` | 把一段规则当成整体，常配合重复次数使用 | ★★ |
| 竖线 | 表示「或」，如 \`^(男 | 女)$\` |

示例：

```sql
-- 性别只能是男或女
WHERE gender REGEXP '^(男|女)$'
-- 3-3-4 格式的号码，也可以用分组表达
WHERE phone REGEXP '^[1-9][0-9]{2}-[0-9]{3}-[0-9]{4}$'
```

### V6. 常用模板

| 用途 | 规则 | 说明 |
| --- | --- | --- |
| 纯数字 | `^[0-9]+$` | 至少一位数字 |
| 4 位年份 | `^[0-9]{4}$` | 只校验格式，不保证是合理年份 |
| 日期格式 | `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` | 只校验格式，不校验月份、日期是否合理 |
| 国内手机号（11 位） | `^1[3-9][0-9]{9}$` | 号段会变化，只作格式参考 |
| 简化邮箱 | `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$` | 只做常见格式判断，不能完全覆盖所有合法邮箱 |
| 首位不为 0 的 10 位数字 | `^[1-9][0-9]{9}$` | SQL40 的连续格式 |
| 3-3-4 格式号码 | `^[1-9][0-9]{2}-[0-9]{3}-[0-9]{4}$` | SQL40 的带连字符格式 |
| 含有数字 | `[0-9]` | 不写 ^$，表示只要包含 |
| 只含字母 | `^[A-Za-z]+$` | 不包含中文 |

### V7. 以 SQL40 为例的完整分析

题目要求：10 位数字，首位不能为 0，格式可以是连续的 10 位，或者 3-3-4 用连字符分隔。

**常见写法的漏洞：**

```sql
WHERE phone_number REGEXP '^[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{4}$'
```

两个连字符是各自独立可选的，所以只有一个连字符的 `123-4567890`、`123456-7890` 也会通过。

**更严格的写法：把两种格式分开写，用 OR 连接。**

```sql
WHERE phone_number REGEXP '^[1-9][0-9]{9}$'
   OR phone_number REGEXP '^[1-9][0-9]{2}-[0-9]{3}-[0-9]{4}$'
```

**不推荐的思路：** 先用 REPLACE 去掉连字符再判断长度，会把 `123-4567-890` 这种连字符位置不对的号码误判为合法。

### V8. 易错点

| 易错点 | 说明 | 频率 |
| --- | --- | --- |
| 忘记 `^` 和 `$` | REGEXP 默认是「包含」匹配，格式校验必须加锚点 | ★★★ |
| 特殊符号没转义 | `.`、`+`、`*`、`?`、`(`、`)`、`[` 等有特殊含义，想表示字面量要加 `\\` | ★★★ |
| 反斜杠要写两遍 | 在 MySQL 字符串里 `\\d` 才是正则的 `\d`；为了少出错，优先用 `[0-9]` | ★★★ |
| 可选符号各自独立 | 多个 `?` 同时使用会产生意料之外的组合，必要时拆成多个分支 | ★★ |
| 大小写问题 | 是否区分大小写取决于字符集和排序规则；需要明确时用 `REGEXP_LIKE` 的选项 | ★★ |
| 贪婪匹配 | `.*` 会尽可能多地匹配；提取片段时要留意 | ★ |
| NULL 值 | 列为 NULL 时，REGEXP 的结果是 NULL，不会被当成匹配成功 | ★★ |
| 性能 | REGEXP 一般用不上索引，大表上慎用；只判断前缀时优先用 `LIKE '前缀%'` | ★★ |
| 中文匹配 | 可以用 Unicode 范围，如 `[\\x{4e00}-\\x{9fa5}]`，不同版本支持情况不一，使用前先自测 | ★ |

### V9. 不同数据库的写法

| 数据库 | 常用写法 |
| --- | --- |
| MySQL | `列 REGEXP '规则'`、`REGEXP_LIKE`（8.0+） |
| PostgreSQL | `列 ~ '规则'`（区分大小写）、`列 ~* '规则'`（不区分） |
| Oracle | `REGEXP_LIKE(列, '规则')` |
| SQL Server | 原生不支持完整的正则，通常用 LIKE 的有限模式或其他函数 |
| Hive / Spark SQL | `列 RLIKE '规则'`、`regexp_extract`、`regexp_replace`，转义需要写双反斜杠 |

### V10. 学习建议

1. 先掌握 `^ $ [ ] { } ? + .` 这几个符号，已经能覆盖大部分笔试题。
2. 写规则时，先把要求拆成「开头、中间各段、结尾」，逐段翻译。
3. 写完用几组正例和反例手推验证，特别是边界情况（多一位、少一位、连字符位置不对）。
4. 复杂的规则可以放到在线正则测试工具里调试，再放进 SQL。

## W. 建表与增删改实操指南（带完整示例）

[↑目录](#m22s1cf5rb4.26697) · [基础](#m22s1cf5rb4.162) · [A](#m22s1cf5rb4.4171) · [B](#m22s1cf5rb4.4724) · [C](#m22s1cf5rb4.5166) · [D](#m22s1cf5rb4.5679) · [E](#m22s1cf5rb4.5912) · [F](#m22s1cf5rb4.6530) · [G](#m22s1cf5rb4.6813) · [H](#m22s1cf5rb4.7436) · [I](#m22s1cf5rb4.8048) · [J](#m22s1cf5rb4.8428) · [K](#m22s1cf5rb4.8794) · [L](#m22s1cf5rb4.9067) · [M](#m22s1cf5rb4.9423) · [N](#m22s1cf5rb4.9941) · [O](#m22s1cf5rb4.10346) · [P](#m22s1cf5rb4.10602) · [Q](#m22s1cf5rb4.10828) · [R](#m22s1cf5rb4.10986) · [S](#m22s1cf5rb4.12551) · [T](#m22s1cf5rb4.13184) · [U](#m22s1cf5rb4.13532) · [V](#m22s1cf5rb4.16599) · [W](#m22s1cf5rb4.19900)

前面的内容以 SELECT 为主。这一节补上建表和数据的增删改，按「从零建一张表 → 插入 → 修改 → 删除 → 改结构」的顺序，方便照着练习和查询。

### W1. 语句分类

| 类型 | 语句 | 作用 | 频率 |
| --- | --- | --- | --- |
| DQL | SELECT | 查询数据 | ★★★ |
| DML | INSERT、UPDATE、DELETE | 增、改、删数据 | ★★★ |
| DDL | CREATE、ALTER、DROP、TRUNCATE | 建、改、删表结构（或清空表） | ★★★ |
| TCL | START TRANSACTION、COMMIT、ROLLBACK | 事务控制 | ★★ |
| DCL | GRANT、REVOKE | 授权，偏运维 | ★ |

数据分析岗以查询为主，但建表、插入、修改和删除也要会，尤其是造测试数据和清洗数据时。

### W2. 先认识环境：库与表

```sql
SHOW DATABASES;                         -- 查看有哪些库
CREATE DATABASE IF NOT EXISTS shop;     -- 建库
USE shop;                               -- 切换到某个库
SHOW TABLES;                            -- 查看当前库有哪些表
DESC students;                          -- 查看表结构（列名、类型、约束）
SHOW CREATE TABLE students;             -- 查看完整建表语句
```

### W3. 建表 CREATE TABLE

```sql
CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INT,
  city VARCHAR(50) DEFAULT '未知',
  score DECIMAL(5, 2),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

每一列的写法是：列名 类型 约束。

| 部分 | 含义 | 频率 |
| --- | --- | --- |
| `INT`、`BIGINT` | 整数，ID 常用 BIGINT | ★★★ |
| `VARCHAR(n)` | 最长 n 个字符的字符串 | ★★★ |
| `DECIMAL(m, n)` | 精确小数，m 是总位数，n 是小数位数，金额必用 | ★★★ |
| `DATE` / `DATETIME` | 日期 / 日期时间 | ★★★ |
| `TEXT` | 长文本 | ★★ |
| `PRIMARY KEY` | 主键，唯一且非空，一张表通常有一个 | ★★★ |
| `AUTO_INCREMENT` | 自增编号，插入时不用管这一列 | ★★★ |
| `NOT NULL` | 不能为空 | ★★★ |
| `DEFAULT 值` | 不写时使用的默认值 | ★★★ |
| `UNIQUE` | 该列值不能重复，如邮箱、手机号 | ★★ |
| `COMMENT '说明'` | 给列加注释，方便团队协作 | ★★ |
| `FOREIGN KEY` | 外键，保证引用的数据存在 | ★★ |
| `CHECK (条件)` | 检查约束，8.0.16 起才真正生效 | ★ |

**易错点：**

1. 最后一列后面**不能有逗号**，这是新手最常见的语法错误。
2. 字符串默认值要加单引号，数字不用。
3. 一张表只能有一个主键，但主键可以由多列组成：`PRIMARY KEY (a, b)`。

**带外键的例子：**

```sql
CREATE TABLE orders (
  order_id BIGINT PRIMARY KEY AUTO_INCREMENT,
  student_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  order_date DATE,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

之后向 orders 插入数据时，`student_id` 必须在 students 表里存在，否则会报外键错误。

### W4. 插入数据 INSERT

```sql
-- 插入一行（建议每次都写列名）
INSERT INTO students (name, age, city) VALUES ('张三', 20, '北京');

-- 一次插入多行
INSERT INTO students (name, age, city, score) VALUES
  ('李四', 21, '上海', 88.5),
  ('王五', 22, '广州', 92),
  ('赵六', 23, NULL, 75.5);

-- 把查询结果插入另一张表
INSERT INTO students_bak (name, age, city)
SELECT name, age, city FROM students WHERE age >= 21;
```

| 要点 | 说明 | 频率 |
| --- | --- | --- |
| 写上列名 | 省略列名时，值必须和所有列按顺序一一对应，表结构一改就容易出错 | ★★★ |
| 自增列不用写 | AUTO\_INCREMENT 的列由数据库自动生成 | ★★★ |
| 没写的列 | 使用默认值，没有默认值则为 NULL；NOT NULL 又没默认值会报错 | ★★★ |
| 字符串和日期 | 用单引号，如 `'2026-11-09'`；字符串里有单引号时写两个：`'It''s'` | ★★★ |
| NULL | 不加引号，表示没有值 | ★★★ |
| `INSERT ... SELECT` | 批量搬运数据，常用于备份和数据迁移 | ★★ |
| `INSERT ... ON DUPLICATE KEY UPDATE` | 主键或唯一键冲突时，改为更新，避免报错 | ★★ |
| `INSERT IGNORE` | 冲突时直接跳过，不报错（会忽略错误，慎用） | ★ |
| `REPLACE INTO` | 冲突时先删后插，会丢掉未写入的列，慎用 | ★ |

```sql
-- 冲突时更新（假设 name 有唯一约束）
INSERT INTO students (name, age) VALUES ('张三', 25)
ON DUPLICATE KEY UPDATE age = VALUES(age);
```

插入后随时用 `SELECT * FROM students;` 检查。

### W5. 修改数据 UPDATE

```sql
-- 改一行的多个字段
UPDATE students SET age = 21, city = '深圳' WHERE name = '张三';

-- 基于原值计算
UPDATE students SET score = score + 5 WHERE city = '上海';

-- 设置为空
UPDATE students SET city = NULL WHERE id = 4;

-- 用 CASE WHEN 一次改多种情况
UPDATE students
SET score = CASE
      WHEN score >= 90 THEN score
      WHEN score >= 80 THEN score + 2
      ELSE score + 5
    END;

-- 多表关联更新（了解即可）
UPDATE students s
JOIN orders o ON s.id = o.student_id
SET s.city = '已下单'
WHERE o.amount > 100;
```

| 要点 | 说明 | 频率 |
| --- | --- | --- |
| **必须带 WHERE** | 否则会修改整张表的所有行 | ★★★ |
| 先 SELECT 再 UPDATE | 用同样的 WHERE 先查一遍，确认选中的行 | ★★★ |
| 多个字段用逗号分隔 | `SET a = 1, b = 2`，不是 AND | ★★★ |
| 可以用 LIMIT | `UPDATE ... LIMIT 10` 限制最多修改的行数，多一层保险 | ★ |
| 事务保护 | 重要修改放进事务，见 W9 | ★★ |

### W6. 删除数据 DELETE

```sql
DELETE FROM students WHERE id = 3;
DELETE FROM students WHERE age < 18 AND city IS NULL;
```

| 要点 | 说明 | 频率 |
| --- | --- | --- |
| **必须带 WHERE** | 否则会删除整张表所有行 | ★★★ |
| 先 SELECT 确认 | 把 DELETE 换成 `SELECT *`，看一下会删掉哪些行 | ★★★ |
| 外键限制 | 如果其他表引用了这行，会删除失败，要先处理被引用的数据，或设置级联 | ★★ |
| 删除重复行 | 常用做法是用窗口函数或临时表保留一条，建议先备份再操作 | ★★ |

### W7. 清空与删表：三者对比

| 语句 | 删什么 | 能否回滚 | 自增编号 | 速度 | 频率 |
| --- | --- | --- | --- | --- | --- |
| `DELETE FROM 表 WHERE ...` | 符合条件的行 | 事务中可以 | 不重置 | 较慢 | ★★★ |
| `TRUNCATE TABLE 表` | 全部数据，保留表结构 | 一般不能 | 重置为从 1 开始 | 快 | ★★ |
| `DROP TABLE 表` | 整张表，包括结构 | 不能 | — | 快 | ★★ |

```sql
TRUNCATE TABLE students;
DROP TABLE IF EXISTS students;     -- IF EXISTS 避免表不存在时报错
```

### W8. 修改表结构 ALTER TABLE

```sql
ALTER TABLE students ADD COLUMN email VARCHAR(100);            -- 加列
ALTER TABLE students ADD COLUMN grade INT AFTER age;           -- 加列并指定位置
ALTER TABLE students MODIFY COLUMN age TINYINT;                -- 改列类型
ALTER TABLE students CHANGE COLUMN city location VARCHAR(50);  -- 改列名，同时要写类型
ALTER TABLE students DROP COLUMN email;                        -- 删列
ALTER TABLE students RENAME TO students_new;                   -- 改表名
ALTER TABLE students ADD UNIQUE (name);                        -- 加唯一约束
ALTER TABLE students ADD INDEX idx_city (city);                -- 加索引
```

| 要点 | 说明 | 频率 |
| --- | --- | --- |
| 改列类型要小心 | 缩小长度或改成不兼容的类型，可能导致数据被截断或报错 | ★★ |
| 删列不可恢复 | 操作前先备份表 | ★★ |
| 大表改结构较慢 | 生产环境要选业务低峰，并请 DBA 评估 | ★ |
| 改列名用 CHANGE | MySQL 8.0 也支持 `RENAME COLUMN 旧名 TO 新名` | ★ |

### W9. 用事务给自己加保险

```sql
START TRANSACTION;
UPDATE students SET age = 99;      -- 手滑，忘了写 WHERE
SELECT * FROM students;            -- 发现不对
ROLLBACK;                          -- 撤销全部修改
-- 确认没有问题，则执行：
-- COMMIT;
```

| 要点 | 说明 | 频率 |
| --- | --- | --- |
| 默认自动提交 | MySQL 每条语句默认自动提交，需要先 `START TRANSACTION` 才有回滚的机会 | ★★★ |
| DDL 会自动提交 | CREATE、ALTER、DROP、TRUNCATE 不能回滚 | ★★★ |
| 只有 InnoDB 支持事务 | 常见表基本都是 InnoDB | ★★ |
| 做完要 COMMIT 或 ROLLBACK | 不要让事务一直开着，会占用资源、锁住数据 | ★★ |

### W10. 常用实用写法

```sql
CREATE TABLE students_bak LIKE students;                 -- 复制表结构（含索引、约束）
INSERT INTO students_bak SELECT * FROM students;         -- 再把数据复制过去

CREATE TABLE students_copy AS SELECT * FROM students;    -- 一步复制结构和数据（索引、约束不会复制）

CREATE TABLE IF NOT EXISTS students (...);               -- 表不存在才创建
```

**修改重要数据前的习惯：** 先用 `CREATE TABLE 表_bak AS SELECT * FROM 表;` 备份一份，再动手。

### W11. 常见报错与处理

| 报错或现象 | 原因 | 怎么处理 | 频率 |
| --- | --- | --- | --- |
| 语法错误，位置在 `)` 附近 | 最后一列后面多了逗号 | 删掉多余逗号 | ★★★ |
| 字符串或日期报错 | 没有加单引号 | 文字和日期都用单引号 | ★★★ |
| `Column count doesn't match value count` | 列数和值的个数不一致 | 数一下两边是否对应 | ★★★ |
| `Duplicate entry` | 主键或唯一键重复 | 去掉重复，或改用 ON DUPLICATE KEY UPDATE | ★★★ |
| `Column cannot be null` | NOT NULL 的列没给值 | 补上值，或给列设默认值 | ★★★ |
| `Data too long for column` | 内容超过列长度 | 缩短内容，或用 ALTER 改大列 | ★★ |
| `Cannot add or update a child row` | 外键引用的数据不存在 | 先插入被引用表的数据 | ★★ |
| `Cannot delete or update a parent row` | 有其他表引用了这一行 | 先处理引用它的数据，或设置级联 | ★★ |
| 在 Workbench 报 Safe Update 错误（1175） | 安全模式要求 UPDATE 或 DELETE 的 WHERE 使用主键条件，或带 LIMIT | 改用主键条件，或谨慎关闭安全模式 | ★★ |
| `Table doesn't exist` | 没有选对库，或表名拼错 | 先 `USE 库名;` 再确认 `SHOW TABLES;` | ★★★ |
| 中文变成乱码或问号 | 字符集不匹配 | 建表时用 `DEFAULT CHARSET = utf8mb4` | ★★ |

### W12. 执行前的检查清单

每次执行修改类语句前，过一遍：

1. 当前连接的是哪个库、哪张表？是不是测试环境？
2. UPDATE 和 DELETE 有没有带 WHERE？
3. 用同样的条件先 SELECT 过吗？选中的行数对不对？
4. 重要数据有没有备份？
5. 能不能放在事务里，先看结果再决定 COMMIT 还是 ROLLBACK？
6. 改结构或清空表前，确认没有其他程序在用这张表。

### W13. 动手练习任务

建议在自己电脑装 MySQL，或使用在线沙盒（如 DB Fiddle，选择 MySQL 8）练习。

1. 建一张 `orders` 表，字段包括 order\_id、user\_id、amount、order\_date。
2. 一次插入 10 行数据，故意包含：金额较大的、较小的、同一用户多笔、日期跨月份、有一行金额为 NULL。
3. 用前面学过的 SELECT、GROUP BY 统计每个用户的订单数和总金额。
4. 把某个用户的订单金额统一加 10，先用 SELECT 确认再 UPDATE。
5. 删除金额为 NULL 的那一行。
6. 用 ALTER 给表增加一列 `status`，默认值为 '已完成'。
7. 开启事务，故意不写 WHERE 修改全表，再用 ROLLBACK 撤销，体会事务的作用。
8. 故意犯几次错：最后一列多写逗号、插入重复主键、给 NOT NULL 列插入 NULL，看看会报什么错，并学会读报错信息。
