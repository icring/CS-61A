-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      select "Your", "Code", "Here"
    )
  select "Your" as start, "Code" as end, "Here" as hops;

select "Lengths of inland paths between CA and WA:";
select * from inland_distances where start = "CA" and end = "WA" order by hops;

select "States 2 inland hops from CA:";
select end from inland_distances where start = "CA" and hops = 2;
