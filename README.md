# Best11_T20_Analysis
Built a complete data analytics pipeline to analyze T20 World Cup 2022 data and identify the best XI players that could represent Earth in a hypothetical match against aliens.

# Parameter Scoping 
Openers
| **Parameter**    | **Description**                   | **Criteria** |
| ---------------- | --------------------------------- | ------------ |
| Batting Average  | Average runs scored in an innings | > 30         |
| Strike Rate      | No. of runs scored per 100 balls  | > 140        |
| Innings Batted   | Total innings batted              | > 3          |
| Boundary %       | % of runs scored in boundaries    | > 50%        |
| Batting Position | Order in which the batter played  | < 4          |

<img width="1304" height="733" alt="Screenshot 2025-07-22 114443" src="https://github.com/user-attachments/assets/cdf16d27-a39c-4200-9202-f0f014e5dfac" />


Anchors / Middle Order
| **Parameter**    | **Description**                   | **Criteria** |
| ---------------- | --------------------------------- | ------------ |
| Batting Average  | Average runs scored in an innings | > 40         |
| Strike Rate      | No. of runs scored per 100 balls  | > 125        |
| Innings Batted   | Total innings batted              | > 3          |
| Avg. Balls Faced | Average balls faced per innings   | > 20         |
| Batting Position | Order in which the batter played  | > 2          |

<img width="1299" height="730" alt="anchors" src="https://github.com/user-attachments/assets/5cbb6300-78b6-41dc-9a85-0f148e14775f" />


Finisher / Lower Order Anchor
| **Parameter**    | **Description**                   | **Criteria** |
| ---------------- | --------------------------------- | ------------ |
| Batting Average  | Average runs scored in an innings | > 25         |
| Strike Rate      | No. of runs scored per 100 balls  | > 130        |
| Innings Batted   | Total innings batted              | > 3          |
| Avg. Balls Faced | Average balls faced per innings   | > 12         |
| Batting Position | Order in which the batter played  | > 4          |
| Innings Bowled   | Total innings bowled              | > 1          |

<img width="1300" height="732" alt="finishers" src="https://github.com/user-attachments/assets/1bc99403-5cc3-4f67-a52f-977a6e6ab177" />


All-Rounders / Lower Order
| **Parameter**       | **Description**                   | **Criteria** |
| ------------------- | --------------------------------- | ------------ |
| Batting Average     | Average runs scored in an innings | > 15         |
| Strike Rate         | No. of runs scored per 100 balls  | > 140        |
| Innings Batted      | Total innings batted              | > 2          |
| Batting Position    | Order in which the batter played  | > 4          |
| Innings Bowled      | Total innings bowled              | > 2          |
| Bowling Economy     | Average runs allowed per over     | < 7          |
| Bowling Strike Rate | Balls required per wicket         | < 20         |

<img width="1298" height="731" alt="all-rounders" src="https://github.com/user-attachments/assets/56c2dff1-1fcb-49cd-9c00-4f49e1aa5328" />


Specialist Fast Bowlers
| **Parameter**       | **Description**               | **Criteria** |
| ------------------- | ----------------------------- | ------------ |
| Innings Bowled      | Total innings bowled          | > 4          |
| Bowling Economy     | Average runs allowed per over | < 7          |
| Bowling Strike Rate | Balls required per wicket     | < 16         |
| Bowling Style       | Bowling style of the player   | = "%Fast%"   |
| Bowling Average     | Runs allowed per wicket       | < 20         |
| Dot Ball %          | % of dot balls bowled         | > 40%        |

<img width="1302" height="731" alt="bowlers" src="https://github.com/user-attachments/assets/b5730bea-b74b-4478-ad6a-77ab89c9773b" />


# Best 11 Team

<img width="1303" height="732" alt="final11" src="https://github.com/user-attachments/assets/009009df-1346-4ee5-9e1a-19a8591f9e0c" />






