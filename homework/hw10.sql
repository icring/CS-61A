-- CS 61A Fall 2014
-- Name: Sony Theakanath
-- Login: cs61a-ach

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------
select "=========QUESTION 1==========";

create table dog_size as 
  select name, size from dogs, sizes where height > min and height <= max;

-- The names of all "toy" and "mini" dogs
select name from dog_size where size = "toy" or size = "mini";
-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

select "=========QUESTION 2==========";
-- All dogs with parents ordered by decreasing height of their parent
select child from parents, dogs where parent = name order by -height;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size


select "=========QUESTION 3==========";

with pair(first, second, type) as (
  select a.child, b.child, c.size from parents as a, parents as b, dog_size as c, dog_size as d
    where a.parent = b.parent and a.child < b.child and a.child = c.name and b.child = d.name and c.size = d.size
)

select first || " and " || second || " are " || type || " siblings" from pair;

-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

select "=========QUESTION 4==========";
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
with stack(list, sum, last, n) as (
   select name, height, height, 1 from dogs union
   select list || ", " || name, sum + height, height, n + 1
     from stack, dogs where last < height
)

select list, sum from stack where n = 4 and sum >= 170 order by sum;

-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

select "=========QUESTION 5==========";

with relation(first, second, last) as (
   select a.name, b.name from dogs, parents
      where a.name != parent and b.name != 
    )

-- All non-parent relations ordered by height difference
--select "REPLACE THIS LINE WITH YOUR SOLUTION";
-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


