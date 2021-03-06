# Quality of Data

## Quality of Data

> Elaborate more!!!

- It needs plenty of queries and of course a lot of time to query Amap url for enough possible points getting real-time life cycles.

## Elasticity Rules

- Queries should be produced in batch or concurrently rather than serially.
  - It can help reduce the burden of our servers.

- Results should be rendered asynchronously. Fetch one result and render one.
  - It can make users feel much better in a simple way rather than adding more servers.

## QoD Metrics

- Q: **Domain-specific metrics**
  - Need specific tools and expertise for determining metrics
- A: We assume that life circle is continuous and uninterrupted. So if we wanna know the edge of 20 minutes life cycle, we can first search one PoInt in one direction for 20 minutes distance, and then we have a rough 20 minutes radius. Then we search the ring around the 20 minutes circle. It can help us reduce query times a lot and better use batch query provided by Amap.

-------------

- Q: **Evaluation**
  - Cannot done by software only: humans are required
  - Exact versus inexact evaluation due to big and streaming data
- A: There are some parameters that still need human to define which is better.

-------------

- Q: **Complex integration model**
  - Where to put QoD evaluators and why?
  - How evaluators obtain the data to be evaluated?
- A: QoD is both needed for the input data and output data. For us, our input is the data from Amap API and our output data is the feedback of the users.

-------------

- Q: **Impact of QoD evaluation on performance of data analytics workflows**
- A: It can help us reduce a lot when querying using Amap API. However, it need much more human attention.

### Tool

- [Telegraf](http://www.telegraf.rs/)
  - store the input evaluation, output and user feedback.

## Where We Use

### Third-Party Service Provider

- Design of APIs: parameters, quantity, output items
- The update frequency and quality
- The review score from the provider, like the comment in OpenStreetMaps

### Output Data

- Calculate the precision by comparing output data with the real value
- Receive the user feedback and suggestion
