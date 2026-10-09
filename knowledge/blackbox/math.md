# BLACK BOX volume: math
# Restart-civilization knowledge. Quality-filtered.

### MATH-01-001
PRINCIPLE: Natural numbers are the set of positive integers used for counting.
FORMULAS: none
REBUILD: Start with the concept of a unit; repeatedly add one to generate successors.
### MATH-01-002
PRINCIPLE: Addition combines two quantities into their total.
FORMULAS: a + b = c
REBUILD: Define addition as repeated succession; verify with counting objects.
### MATH-01-003
PRINCIPLE: Subtraction finds the difference by removing a quantity from another.
FORMULAS: a - b = c (where a ≥ b)
REBUILD: Define as inverse of addition; check by adding back.
### MATH-01-004
PRINCIPLE: Multiplication is repeated addition of equal groups.
FORMULAS: a × b = c
REBUILD: Construct by adding a to itself b times; use arrays.
### MATH-01-005
PRINCIPLE: Division splits a quantity into equal parts.
FORMULAS: a ÷ b = c (b ≠ 0)
REBUILD: Define as inverse of multiplication; test by multiplying divisor and quotient.
### MATH-01-006
PRINCIPLE: A fraction represents a part of a whole as numerator over denominator.
FORMULAS: a/b where b ≠ 0
REBUILD: Partition a unit into b equal parts; take a parts.
### MATH-01-007
PRINCIPLE: Decimals express fractions with denominators powers of ten using place value.
FORMULAS: 0.d1d2... = Σ di × 10^{-i}
REBUILD: Extend the place‑value system right of the units place; interpret each digit as tenths, hundredths, etc.
### MATH-01-008
PRINCIPLE: A percentage is a fraction with denominator 100, denoted by %.
FORMULAS: p% = p/100
REBUILD: Convert a ratio to parts per hundred by multiplying by 100 and adding the % sign.
### MATH-01-009
PRINCIPLE: A ratio compares two quantities by division.
FORMULAS: a : b = a/b
REBUILD: Express the relative size of a to b; simplify by dividing both by their GCD.
### MATH-01-010
PRINCIPLE: A prime number is a natural >1 with no divisors other than 1 and itself.
FORMULAS: none
REBUILD: Test divisibility by all integers up to √n; if none divide, n is prime.
### MATH-01-011
PRINCIPLE: A factor divides a number exactly; a multiple is a product of that number.
FORMULAS: if a|b then b = a×k; multiples: n×k
REBUILD: List all integers k such that n×k gives multiples; factor by checking divisibility.
### MATH-01-012
PRINCIPLE: Exponentiation repeats multiplication of a base.
FORMULAS: a^n = a × a × ... × a (n times)
REBUILD: Define a^0 = 1; a^{n+1} = a^n × a; extend to negative and fractional exponents via reciprocals and roots.
### MATH-01-013
PRINCIPLE: The nth root of a is the number whose nth power equals a.
FORMULAS: √[n]{a} = b ⇔ b^n = a
REBUILD: For n=2, use guess‑and‑check or Babylonian method; generalize via exponent 1/n.
### MATH-01-014
PRINCIPLE: Expressions are evaluated using a fixed hierarchy: parentheses, exponents, multiplication/division, addition/subtraction.
FORMULAS: PEMDAS
REBUILD: Apply the hierarchy step‑by‑step to any arithmetic expression to obtain a unique result.
### MATH-01-015
PRINCIPLE: Addition and multiplication obey commutative, associative, and distributive laws.
FORMULAS: a+b=b+a; (a+b)+c=a+(b+c); a×(b+c)=a×b+a×c
REBUILD: Verify each law with arbitrary numbers; use them to rearrange and simplify expressions.
### MATH-02-001
PRINCIPLE: A variable symbol stands for an unknown or varying quantity; expressions combine variables, numbers, and operations.
FORMULAS: e.g., 2x + 3
REBUILD: Choose a symbol to represent a quantity; write arithmetic combinations to model relationships.
### MATH-02-002
PRINCIPLE: Substitute given values for variables and compute using order of operations.
FORMULAS: none
REBUILD: Replace each variable with its value, then follow PEMDAS to obtain a number.
### MATH-02-003
PRINCIPLE: Two expressions are equivalent if they yield the same value for all variable assignments.
FORMULAS: none
REBUILD: Use properties (commutative, associative, distributive) to transform one expression into another; check equality symbolically.
### MATH-02-004
PRINCIPLE: A linear equation has the form ax + b = 0 with a ≠ 0.
FORMULAS: ax + b = 0 → x = -b/a
REBUILD: Isolate the variable by inverse operations; solve for x.
### MATH-02-005
PRINCIPLE: Collect variable terms on one side and constants on the other.
FORMULAS: ax + b = cx + d → (a-c)x = d-b → x = (d-b)/(a-c) if a≠c
REBUILD: Subtract cx from both sides, subtract b, then divide by (a-c).
### MATH-02-006
PRINCIPLE: Inequalities compare expressions; solving follows similar steps, reversing sign when multiplying/dividing by negative.
FORMULAS: ax + b < c
REBUILD: Isolate variable; if multiply/divide by negative, flip inequality direction.
### MATH-02-007
PRINCIPLE: A solution satisfies both equations simultaneously.
FORMULAS: { a1x + b1y = c1; a2x + b2y = c2 }
REBUILD: Use substitution or elimination: solve one for a variable, plug into the other, or add/subtract to eliminate.
### MATH-02-008
PRINCIPLE: A quadratic equation is ax^2 + bx + c = 0 with a ≠ 0.
FORMULAS: x = [-b ± √(b^2 - 4ac)]/(2a)
REBUILD: Compute discriminant; apply quadratic formula; factor if possible.
### MATH-02-009
PRINCIPLE: Express ax^2+bx+c as product of linear factors when possible.
FORMULAS: ax^2+bx+c = (dx+e)(fx+g)
REBUILD: Find two numbers whose product = ac and sum = b; split middle term and factor by grouping.
### MATH-02-010
PRINCIPLE: A function maps each input to exactly one output; written f(x).
FORMULAS: y = f(x)
REBUILD: Define a rule that assigns a unique output for each permissible input; verify vertical line test.
### MATH-02-011
PRINCIPLE: Linear functions have constant rate of change; graph is a straight line.
FORMULAS: f(x) = mx + b
REBUILD: Identify slope m and y-intercept b; plot points or use rise-over-run.
### MATH-02-012
PRINCIPLE: Quadratic functions form parabolas; vertex gives max/min.
FORMULAS: f(x) = ax^2 + bx + c
REBUILD: Determine axis of symmetry x = -b/(2a); compute vertex; plot points.
### MATH-02-013
PRINCIPLE: Exponential functions grow or decay by a constant factor per unit interval.
FORMULAS: f(x) = a·b^x (b>0, b≠1)
REBUILD: Start with initial value a; multiply by b for each increment of x.
### MATH-02-014
PRINCIPLE: Polynomials are sums of terms a_n x^n with non‑negative integer exponents.
FORMULAS: Σ_{i=0}^n a_i x^i
REBUILD: Combine like terms; arrange in descending degree; factor using GCF, grouping, or special products.
### MATH-02-015
PRINCIPLE: Rational expressions are ratios of polynomials; simplify by canceling common factors.
FORMULAS: P(x)/Q(x), Q(x)≠0
REBUILD: Factor numerator and denominator; divide out any common polynomial factors.
### MATH-03-001
PRINCIPLE: Points have no size; lines extend infinitely in two directions; planes are flat infinite surfaces.
FORMULAS: none
REBUILD: Define point as location; line as set of points extending in two opposite directions; plane as set of points satisfying a linear equation.
### MATH-03-002
PRINCIPLE: A segment has two endpoints; a ray has one endpoint and extends infinitely in one direction.
FORMULAS: none
REBUILD: Choose two points for a segment; choose an endpoint and direction for a ray.
### MATH-03-003
PRINCIPLE: An angle is formed by two rays sharing a vertex; measured in degrees or radians.
FORMULAS: θ = (arc length)/radius (radians)
REBUILD: Draw two rays from a point; quantify the rotation needed to align one with the other.
### MATH-03-004
PRINCIPLE: Classification by measure: <90°, =90°, >90°<180°, =180°.
FORMULAS: none
REBUILD: Compare angle measure to 90° and 180° thresholds.
### MATH-03-005
PRINCIPLE: Parallel lines never intersect; perpendicular lines intersect at 90°.
FORMULAS: slopes m1=m2 (parallel); m1·m2 = -1 (perpendicular) in coordinate plane.
REBUILD: In Euclidean geometry, construct using a compass and straightedge; in coordinates, compare slopes.
### MATH-03-006
PRINCIPLE: Triangles are three‑sided polygons; classified as scalene, isosceles, equilateral.
FORMULAS: none
REBUILD: Connect three non‑collinear points; compare side lengths.
### MATH-03-007
PRINCIPLE: Triangles classified as acute, right, obtuse based on angle measures.
FORMULAS: none
REBUILD: Measure each angle; if one equals 90° → right; if >90° → obtuse; else acute.
### MATH-03-008
PRINCIPLE: In a right triangle, the square of the hypotenuse equals sum of squares of legs.
FORMULAS: a^2 + b^2 = c^2
REBUILD: Construct squares on each side; show area equality via rearrangement or similarity.
### MATH-03-009
PRINCIPLE: Triangles are congruent if corresponding sides and angles match under specific criteria.
FORMULAS: none
REBUILD: Verify three corresponding parts (SSS, SAS, ASA, AAS) to conclude congruence.
### MATH-03-010
PRINCIPLE: Similar triangles have equal corresponding angles and proportional sides.
FORMULAS: a1/a2 = b1/b2 = c1/c2
REBUILD: Check two angles equal (AA) or proportional sides with included angle equal.
### MATH-03-011
PRINCIPLE: Quadrilaterals are four‑sided polygons; include squares, rectangles, parallelograms, trapezoids.
FORMULAS: none
REBUILD: Connect four points in order, ensuring sides only meet at vertices.
### MATH-03-012
PRINCIPLE: Area equals base times height.
FORMULAS: A = b × h
REBUILD: Multiply the length of base by the perpendicular height.
### MATH-03-013
PRINCIPLE: Area is half base times height.
FORMULAS: A = ½ b h
REBUILD: Duplicate triangle to form a parallelogram; halve its area.
### MATH-03-014
PRINCIPLE: Circle area = πr^2; circumference = 2πr.
FORMULAS: A = πr^2; C = 2πr
REBUILD: Measure radius; apply formulas; for circumference, multiply diameter by π.
### MATH-03-015
PRINCIPLE: Volume = base area × height.
FORMULAS: V_rect = l w h; V_cyl = π r^2 h
REBUILD: Compute area of base (rectangle or circle); multiply by height.
### MATH-04-001
PRINCIPLE: A limit describes the value a function approaches as the input nears a point.
FORMULAS: lim_{x→a} f(x) = L
REBUILD: Examine f(x) values from both sides as x→a; if they converge to same number, that's the limit.
### MATH-04-002
PRINCIPLE: Left‑hand and right‑hand limits consider approach from negative or positive side.
FORMULAS: lim_{x→a^-} f(x) = L^- ; lim_{x→a^+} f(x) = L^+
REBUILD: Evaluate f(x) for x<a approaching a, and for x>a approaching a separately.
### MATH-04-003
PRINCIPLE: A function is continuous at a if limit equals function value.
FORMULAS: lim_{x→a} f(x) = f(a)
REBUILD: Check three conditions: f(a) defined, limit exists, and they are equal.
### MATH-04-004
PRINCIPLE: Derivative gives instantaneous rate of change; slope of tangent line.
FORMULAS: f'(x) = lim_{h→0} (f(x+h)-f(x))/h
REBUILD: Compute difference quotient; take limit as h→0.
### MATH-04-005
PRINCIPLE: Derivative of x^n is n x^{n-1}.
FORMULAS: d/dx x^n = n x^{n-1}
REBUILD: Apply limit definition or use binomial expansion; verify for integer n.
### MATH-04-006
PRINCIPLE: Derivative of product of two functions.
FORMULAS: (fg)' = f' g + f g'
REBUILD: Compute limit of (f(x+h)g(x+h)-f(x)g(x))/h; add and subtract f(x)g(x+h).
### MATH-04-007
PRINCIPLE: Derivative of quotient of two functions.
FORMULAS: (f/g)' = (f' g - f g')/g^2
REBUILD: Write quotient as f·g^{-1}; apply product and chain rules.
### MATH-04-008
PRINCIPLE: Derivative of composite function f(g(x)).
FORMULAS: d/dx f(g(x)) = f'(g(x))·g'(x)
REBUILD: Differentiate outer function evaluated at inner, multiply by derivative of inner.
### MATH-04-009
PRINCIPLE: Derivatives of sin, cos, tan, etc.
FORMULAS: d/dx sin x = cos x; d/dx cos x = -sin x; d/dx tan x = sec^2 x
REBUILD: Use limit definitions and trigonometric identities.
### MATH-04-010
PRINCIPLE: Differentiate both sides of an equation relating x and y, treating y as function of x.
FORMULAS: d/dx [F(x,y)] = 0 → solve for dy/dx
REBUILD: Apply derivative to each term, using chain rule for y terms; isolate dy/dx.
### MATH-04-011
PRINCIPLE: Rates of change of linked quantities are related via differentiation.
FORMULAS: differentiate equation linking variables w.r.t. time
REBUILD: Write equation connecting quantities; differentiate implicitly with respect to t; substitute known rates.
### MATH-04-012
PRINCIPLE: Antiderivative reverses differentiation; includes constant C.
FORMULAS: ∫ f(x) dx = F(x) + C where F' = f
REBUILD: Guess a function whose derivative matches f; verify by differentiating.
### MATH-04-013
PRINCIPLE: Definite integral gives net area under curve between limits.
FORMULAS: ∫_a^b f(x) dx = F(b)-F(a) (Fundamental Theorem)
REBUILD: Find antiderivative F; evaluate at b and a; subtract.
### MATH-04-014
PRINCIPLE: Differentiation and integration are inverse processes.
FORMULAS: d/dx ∫_a^x f(t) dt = f(x)
REBUILD: Define accumulation function; show its derivative recovers integrand.
### MATH-04-015
PRINCIPLE: Substitution simplifies integrals by reversing chain rule.
FORMULAS: ∫ f(g(x)) g'(x) dx = ∫ f(u) du with u=g(x)
REBUILD: Choose inner function u; compute du; rewrite integral in u; integrate; back‑substitute.

### MATH-05-001
PRINCIPLE: Each digit's value depends on its position relative to the decimal point, powers of ten.
FORMULAS: value = Σ digit_i × 10^{position_i} (positions left of decimal positive, right negative).
REBUILD: Write number, label places from rightmost digit as ones (10^0), then tens (10^1), hundreds (10^2), etc.; for digits after decimal, use tenths (10^{-1}), hundredths (10^{-2}), etc.; sum contributions.

### MATH-05-002
PRINCIPLE: To add/subtract fractions, convert to common denominator then combine numerators.
FORMULAS: a/b ± c/d = (ad ± bc) / (bd).
REBUILD: Find LCM of denominators, rewrite each fraction with that denominator, add/subtract numerators, keep denominator, simplify if possible.

### MATH-05-003
PRINCIPLE: Multiply fractions by multiplying numerators and denominators; divide by multiplying by reciprocal.
FORMULAS: (a/b) × (c/d) = ac / bd; (a/b) ÷ (c/d) = ad / bc.
REBUILD: For multiplication, multiply top numbers together and bottom numbers together; for division, flip second fraction then multiply; reduce result.

### MATH-05-004
PRINCIPLE: Volume equals area of base times height, or product of length, width, height.
FORMULAS: V = l × w × h.
REBUILD: Measure length, width, height in same units, multiply them; result is cubic units.

### MATH-05-005
PRINCIPLE: Points are located by ordered pairs (x, y) indicating horizontal and vertical distance from origin.
FORMULAS: point = (x, y) where x ≥ 0, y ≥ 0.
REBUILD: Draw two perpendicular axes labeled x (horizontal) and y (vertical); mark equal intervals; locate x coordinate along x-axis, then move vertically to y coordinate; plot point.

### MATH-05-006
PRINCIPLE: Sequences follow a rule that relates each term to its position or previous term.
FORMULAS: arithmetic: a_n = a_1 + (n-1)d; geometric: a_n = a_1 × r^{n-1}.
REBUILD: Identify if pattern adds constant (difference) or multiplies constant (ratio); use appropriate formula to compute any term.

### MATH-05-007
PRINCIPLE: Convert between units using conversion factors that equal 1.
FORMULAS: quantity_new = quantity_old × (conversion factor).
REBUILD: Write known equivalence (e.g., 12 in = 1 ft) as fraction, multiply original measurement by appropriate fraction to cancel old units, keep desired units.

### MATH-05-008
PRINCIPLE: Line plots display frequency of data values along a number line.
FORMULAS: none.
REBUILD: Draw a number line covering data range; for each data point, place an X (or dot) above its value; stack multiple Xs for repeats.

### MATH-05-009
PRINCIPLE: 2D shapes are classified by number of sides and angle properties.
FORMULAS: none.
REBUILD: Count sides; measure angles; name shape: triangle (3), quadrilateral (4), pentagon (5), etc.; note right, acute, obtuse angles.

### MATH-05-010
PRINCIPLE: Triangles are classified by side lengths (equilateral, isosceles, scalene) and angles (acute, right, obtuse).
FORMULAS: none.
REBUILD: Measure three sides; if all equal → equilateral; if two equal → isosceles; else scalene; measure angles; if one 90° → right; if >90° → obtuse; else acute.

### MATH-05-011
PRINCIPLE: Quadrilaterals are sorted by parallel sides, angle measures, and side equality.
FORMULAS: none.
REBUILD: Check for one pair of parallel sides → trapezoid; two pairs → parallelogram; if also right angles → rectangle; if also all sides equal → square; if equal sides but not right angles → rhombus.

### MATH-05-012
PRINCIPLE: Factors divide a number exactly; multiples are products of the number with integers.
FORMULAS: if a × b = n then a and b are factors of n; n = k × m gives multiples.
REBUILD: To find factors, test integers up to √n; to find multiples, multiply n by 1,2,3,...

### MATH-05-013
PRINCIPLE: Prime numbers have exactly two distinct factors (1 and itself); composites have more.
FORMULAS: none.
REBUILD: Check divisibility by primes ≤ √n; if none divide, it's prime; else composite.

### MATH-05-014
PRINCIPLE: Evaluate expressions using PEMDAS/BODMAS to ensure consistent results.
FORMULAS: none.
REBUILD: First parentheses, then exponents, then multiplication/division left to right, then addition/subtraction left to right.

### MATH-05-015
PRINCIPLE: Translate word problems into arithmetic operations using known quantities.
FORMULAS: none.
REBUILD: Identify what is asked, determine relevant numbers, choose operation(s) (+,−,×,÷) based on context, compute, check reasonableness.

### MATH-06-001
PRINCIPLE: A ratio compares two quantities; a rate is a ratio with different units.
FORMULAS: ratio a:b = a/b; rate = quantity1 / quantity2 (units differ).
REBUILD: Write comparison as fraction; simplify if needed; for rate, ensure units included.

### MATH-06-002
PRINCIPLE: A unit rate expresses how much of one quantity corresponds to one unit of another.
FORMULAS: unit rate = a / b where b = 1.
REBUILD: Divide the first quantity by the second; label with per unit of second.

### MATH-06-003
PRINCIPLE: Percent represents a part per hundred.
FORMULAS: p% = p/100; part = percent × whole.
REBUILD: To find percent, divide part by whole and multiply by 100; to find part, multiply percent (as decimal) by whole.

### MATH-06-004
PRINCIPLE: Dividing by a fraction equals multiplying by its reciprocal.
FORMULAS: a/b ÷ c/d = ad / bc.
REBUILD: Flip divisor fraction, then multiply numerators and denominators; simplify.

### MATH-06-005
PRINCIPLE: Add, subtract, multiply, divide decimals by aligning place values.
FORMULAS: addition/subtraction: align decimal points; multiplication: ignore decimals, multiply, then place decimal point sum of decimal places; division: make divisor whole by shifting decimals equally.
REBUILD: For add/sub, line up decimals; for mult, multiply as whole numbers then count total decimal places; for div, shift decimal to make divisor whole, adjust dividend similarly, then divide.

### MATH-06-006
PRINCIPLE: Negative numbers represent values less than zero; absolute value gives distance from zero.
FORMULAS: |x| = x if x ≥ 0, else -x.
REBUILD: To add/subtract negatives, use number line or rules: adding negative subtracts; subtracting negative adds; absolute value removes sign.

### MATH-06-007
PRINCIPLE: The plane is divided into four quadrants by x and y axes; points have signed coordinates.
FORMULAS: quadrant I (+,+), II (−,+), III (−,−), IV (+,−).
REBUILD: Draw axes, label positive right/up, negative left/down; plot (x,y) by moving x horizontally then y vertically.

### MATH-06-008
PRINCIPLE: Algebraic expressions combine numbers, variables, and operations to represent values.
FORMULAS: none.
REBUILD: Identify quantities and operations described; translate to symbols; substitute values for variables and compute using order of operations.

### MATH-06-009
PRINCIPLE: One-step equations are solved by applying the inverse operation to isolate the variable.
FORMULAS: x + a = b → x = b − a; x − a = b → x = b + a; ax = b → x = b/a; x/a = b → x = ab.
REBUILD: Determine operation on variable, apply its inverse to both sides, simplify.

### MATH-06-010
PRINCIPLE: Inequalities show relative size; solving follows similar steps as equations, but multiplying/dividing by negative flips sign.
FORMULAS: none.
REBUILD: Isolate variable using inverse operations; if you multiply/divide by a negative, reverse inequality direction.

### MATH-06-011
PRINCIPLE: Area formulas derive from base times height, adjusted for shape.
FORMULAS: Triangle: A = ½ bh; Parallelogram: A = bh; Trapezoid: A = ½ (b1 + b2)h.
REBUILD: Identify base(s) and perpendicular height; plug into appropriate formula; compute.

### MATH-06-012
PRINCIPLE: Volume of any prism equals base area times height.
FORMULAS: V = B × h where B is area of base.
REBUILD: Compute area of base shape (using its formula), multiply by prism height.

### MATH-06-013
PRINCIPLE: Surface area is sum of areas of all faces.
FORMULAS: For rectangular prism: SA = 2lw + 2lh + 2wh.
REBUILD: Calculate area of each distinct face, add them; for prisms, use formula 2×(areas of three different faces).

### MATH-06-014
PRINCIPLE: Mean is average, median middle value, mode most frequent.
FORMULAS: mean = Σx_i / n; median = middle of ordered data; mode = value with highest frequency.
REBUILD: To find mean, sum all values divide by count; median, order data and pick middle (or average two middles); mode, identify most common value.

### MATH-06-015
PRINCIPLE: Variability measures spread of data around center.
FORMULAS: range = max − min; IQR = Q3 − Q1; MAD = Σ|x_i − mean| / n.
REBUILD: Order data; range subtract smallest from largest; find Q1 (median of lower half) and Q3 (median of upper half) for IQR; compute absolute deviations from mean, average for MAD.

### MATH-07-001
PRINCIPLE: Two quantities are proportional if their ratio is constant.
FORMULAS: y = kx where k is constant of proportionality.
REBUILD: Check if y/x is same for all pairs; if so, relationship is proportional with k = that ratio.

### MATH-07-002
PRINCIPLE: The constant k relates proportional variables as y = kx.
FORMULAS: k = y/x.
REBUILD: Divide y by x for any pair; verify consistency; use k to predict unknowns.

### MATH-07-003
PRINCIPLE: A scale drawing represents actual lengths reduced or enlarged by a constant factor.
FORMULAS: drawing length = actual length × scale factor; actual length = drawing length / scale factor.
REBUILD: Measure drawing length, divide by scale factor to get actual; or multiply actual by scale factor for drawing.

### MATH-07-004
PRINCIPLE: Percent change compares difference to original amount.
FORMULAS: percent change = ((new − old) / old) × 100%.
REBUILD: Subtract old from new, divide by old, multiply by 100; positive → increase, negative → decrease.

### MATH-07-005
PRINCIPLE: Add/subtract rational numbers by finding common denominator.
FORMULAS: a/b ± c/d = (ad ± bc) / bd.
REBUILD: Same as fraction addition/subtraction; apply to positive/negative fractions.

### MATH-07-006
PRINCIPLE: Multiply/divide rational numbers using numerator/denominator rules; sign rules apply.
FORMULAS: (a/b) × (c/d) = ac / bd; (a/b) ÷ (c/d) = ad / bc.
REBUILD: Multiply numerators and denominators; for division, flip second fraction; apply sign: like signs give positive, unlike give negative.

### MATH-07-007
PRINCIPLE: Like terms (same variable powers) can be combined; distributive property expands a(b±c)=ab±ac.
FORMULAS: a(b + c) = ab + ac; a(b − c) = ab − ac.
REBUILD: Identify terms with identical variable parts, add coefficients; use distributive to remove parentheses then combine.

### MATH-07-008
PRINCIPLE: Two-step equations require two inverse operations to isolate variable.
FORMULAS: ax + b = c → x = (c − b)/a; x/a + b = c → x = a(c − b).
REBUILD: Undo addition/subtraction first, then multiplication/division (or vice versa depending on order).

### MATH-07-009
PRINCIPLE: Solve two-step inequalities like equations, remembering to flip sign when multiplying/dividing by negative.
FORMULAS: none.
REBUILD: Isolate variable using inverse operations in reverse order of operations; if you multiply/divide by a negative, reverse inequality.

### MATH-07-010
PRINCIPLE: Complementary angles sum to 90°, supplementary to 180°, vertical angles are equal.
FORMULAS: complement: ∠A + ∠B = 90°; supplement: ∠A + ∠B = 180°; vertical: ∠1 = ∠2.
REBUILD: If one angle known, subtract from 90 or 180 to find complement/supplement; vertical angles are opposite each other at intersection.

### MATH-07-011
PRINCIPLE: In any triangle, side lengths satisfy triangle inequality and angles sum to 180°.
FORMULAS: a + b > c, a + c > b, b + c > a; ∠A + ∠B + ∠C = 180°.
REBUILD: To check if three lengths form triangle, ensure each pair sum > third; to find missing angle, subtract known sum from 180.

### MATH-07-012
PRINCIPLE: Circle's circumference and area relate to radius via π.
FORMULAS: C = 2πr or πd; A = πr^2.
REBUILD: Measure radius; circumference = 2 × π × r; area = π × r × r.

### MATH-07-013
PRINCIPLE: Scaling lengths by factor k scales area by k^2 and volume by k^3.
FORMULAS: Area_scale = k^2 × original area; Volume_scale = k^3 × original volume.
REBUILD: Determine length scale factor; square it for area change, cube it for volume change.

### MATH-07-014
PRINCIPLE: Probability of a simple event equals favorable outcomes divided by total equally likely outcomes.
FORMULAS: P(E) = f / n.
REBUILD: Count number of ways event can happen, count total possible outcomes, divide.

### MATH-07-015
PRINCIPLE: For independent events, probability of both occurring is product of their probabilities.
FORMULAS: P(A and B) = P(A) × P(B) if independent.
REBUILD: Verify independence; multiply individual probabilities; for mutually exclusive, add.

### MATH-08-001
PRINCIPLE: Solve linear equations by isolating variable using inverse operations.
FORMULAS: ax + b = c → x = (c − b)/a.
REBUILD: Subtract b from both sides, then divide by a.

### MATH-08-002
PRINCIPLE: y = mx + b shows slope m and y-intercept b.
FORMULAS: y = mx + b.
REBUILD: Identify slope (rise/run) and intercept (where line crosses y-axis); write equation.

### MATH-08-003
PRINCIPLE: Point-slope form uses a point and slope to define a line.
FORMULAS: y − y1 = m(x − x1).
REBUILD: Plug known point (x1,y1) and slope m into formula; simplify if needed.

### MATH-08-004
PRINCIPLE: Solve one equation for a variable, substitute into the other.
FORMULAS: none.
REBUILD: Choose equation, isolate x or y, plug expression into other equation, solve for remaining variable, then back-substitute.

### MATH-08-005
PRINCIPLE: Add or subtract equations to eliminate one variable.
FORMULAS: none.
REBUILD: Multiply equations if needed to align coefficients, then add/subtract to cancel a variable, solve for other, substitute back.

### MATH-08-006
PRINCIPLE: A function assigns exactly one output to each input.
FORMULAS: f(x) = y.
REBUILD: Check that each input value maps to one output; represent as table, graph, or equation.

### MATH-08-007
PRINCIPLE: Linear functions have constant rate of change and graph as straight line; nonlinear do not.
FORMULAS: linear: y = mx + b; nonlinear: e.g., y = x^2.
REBUILD: Calculate successive differences; if constant, linear; else nonlinear; or graph and see if straight.

### MATH-08-008
PRINCIPLE: Transformations move or flip figures without changing size or shape.
FORMULAS: translation: (x, y) → (x + a, y + b); reflection over x-axis: (x, y) → (x, −y); over y-axis: (−x, y); rotation 90° about origin: (x, y) → (−y, x).
REBUILD: Apply rule to each vertex; plot new points; connect.

### MATH-08-009
PRINCIPLE: Congruent figures have same size and shape; similar have same shape, proportional sizes.
FORMULAS: congruence: corresponding sides equal, angles equal; similarity: corresponding angles equal, sides proportional (ratio k).
REBUILD: For congruence, verify side lengths and angles match; for similarity, check angles equal and compute side ratios constant.

### MATH-08-010
PRINCIPLE: In a right triangle, square of hypotenuse equals sum of squares of legs.
FORMULAS: a^2 + b^2 = c^2.
REBUILD: Identify legs a,b and hypotenuse c; square legs, sum, take square root for c; or rearrange to find leg.

### MATH-08-011
PRINCIPLE: Volume formulas derive from base area times height (cylinder, cone) or radius cubed (sphere).
FORMULAS: Cylinder: V = πr^2 h; Cone: V = (1/3)πr^2 h; Sphere: V = (4/3)πr^3.
REBUILD: Measure radius and height (if applicable); plug into formula; compute.

### MATH-08-012
PRINCIPLE: Surface area sums areas of all faces; formulas exist for common solids.
FORMULAS: Cylinder: SA = 2πr^2 + 2πrh; Cone: SA = πr^2 + πrℓ (ℓ slant height); Sphere: SA = 4πr^2.
REBUILD: Calculate area of each component (bases, lateral surface) using radius, height, slant height; add.

### MATH-08-013
PRINCIPLE: Scatter plots show relationship between two variables; line of best fit models trend.
FORMULAS: line: y = mx + b (least squares).
REBUILD: Plot points; draw line that minimizes distance (roughly through middle); estimate slope and intercept.

### MATH-08-014
PRINCIPLE: Two-way tables organize counts for two categorical variables.
FORMULAS: none.
REBUILD: List categories of one variable as rows, other as columns; fill cell with count of observations matching both.

### MATH-08-015
PRINCIPLE: Irrational numbers cannot be expressed as fraction; radicals often irrational; approximate via decimal.
FORMULAS: none.
REBUILD: Identify if radicand is perfect square; if not, estimate between consecutive integers; refine using averaging or calculator.

### MATH-09-001
PRINCIPLE: Real numbers include all rational and irrational numbers, forming a complete ordered field.
FORMULAS: a + b = b + a; a·b = b·a; a + (b + c) = (a + b) + c; a·(b·c) = (a·b)·c; a·(b + c) = a·b + a·c
REBUILD: Define natural numbers, extend to integers via additive inverses, to rationals via ratios, then to reals via Dedekind cuts or Cauchy sequences.

### MATH-09-002
PRINCIPLE: An algebraic expression combines constants, variables, and arithmetic operations to represent a value.
FORMULAS: none
REBUILD: Identify terms, coefficients, and like terms; apply distributive, associative, and commutative laws to simplify.

### MATH-09-003
PRINCIPLE: A linear equation in one variable has the form ax + b = 0 and yields a unique solution when a ≠ 0.
FORMULAS: x = -b/a
REBUILD: Isolate the variable by performing inverse operations: subtract b, then divide by a.

### MATH-09-004
PRINCIPLE: Linear inequalities compare expressions using <, >, ≤, ≥ and solutions form intervals on the number line.
FORMULAS: none
REBUILD: Solve as an equation, then reverse inequality sign when multiplying/dividing by a negative; test intervals.

### MATH-09-005
PRINCIPLE: A system of two linear equations finds the intersection point of their lines, if any.
FORMULAS: a₁x + b₁y = c₁; a₂x + b₂y = c₂
REBUILD: Use substitution or elimination: solve one equation for a variable, substitute into the other, then back‑substitute.

### MATH-09-006
PRINCIPLE: A quadratic equation ax² + bx + c = 0 has solutions given by the quadratic formula.
FORMULAS: x = (-b ± √(b² - 4ac)) / (2a)
REBUILD: Compute discriminant D = b² - 4ac; if D ≥ 0, evaluate the formula; if D < 0, solutions are complex.

### MATH-09-007
PRINCIPLE: A function maps each input from a domain to exactly one output in a codomain.
FORMULAS: f(x) = y
REBUILD: Define domain, assign a rule that yields a single output for each input, verify uniqueness.

### MATH-09-008
PRINCIPLE: An exponential function has the form f(x) = a·bˣ with constant base b > 0, b ≠ 1.
FORMULAS: f(x) = a·bˣ
REBUILD: Choose initial value a and base b; compute successive values by multiplying by b for each increment in x.

### MATH-09-009
PRINCIPLE: A logarithmic function is the inverse of an exponential, written f(x) = log_b(x) for b > 0, b ≠ 1.
FORMULAS: y = log_b(x) ⇔ bʸ = x
REBUILD: Select base b; define log_b(x) as the exponent y satisfying bʸ = x; compute using change‑of‑base if needed.

### MATH-09-010
PRINCIPLE: A polynomial is a sum of terms cᵢxⁱ where coefficients cᵢ are constants and i is a non‑negative integer.
FORMULAS: P(x) = Σ₀ⁿ cᵢxⁱ
REBUILD: Choose degree n and coefficients; evaluate by substituting x and summing powers multiplied by coefficients.

### MATH-09-011
PRINCIPLE: Factoring rewrites a polynomial as a product of lower‑degree polynomials using identities and common factors.
FORMULAS: none
REBUILD: Extract greatest common factor, then apply difference of squares, perfect square trinomials, or grouping.

### MATH-09-012
PRINCIPLE: A rational expression is a ratio of two polynomials, undefined where the denominator equals zero.
FORMULAS: R(x) = P(x) / Q(x), Q(x) ≠ 0
REBUILD: Factor numerator and denominator, cancel common factors, state excluded values from denominator zeros.

### MATH-09-013
PRINCIPLE: A radical expression involves roots, written √[n]{x}, representing the number whose nth power equals x.
FORMULAS: (√[n]{x})ⁿ = x
REBUILD: For even n, restrict x ≥ 0; for odd n, allow all real x; simplify by factoring perfect nth powers.

### MATH-09-014
PRINCIPLE: Geometry studies points, lines, planes, and angles, with axioms defining incidence and measure.
FORMULAS: none
REBUILD: Accept undefined terms point, line, plane; adopt axioms (e.g., through any two points exactly one line); define angle as union of two rays.

### MATH-09-015
PRINCIPLE: Triangles are classified by side lengths (scalene, isosceles, equilateral) and angles (acute, right, obtuse); congruence criteria include SSS, SAS, ASA.
FORMULAS: none
REBUILD: Measure three sides or two sides and included angle; apply SSS, SAS, ASA, AAS, or HL to test congruence.

### MATH-10-001
PRINCIPLE: A linear function f(x) = mx + b graphs as a straight line with slope m and y‑intercept b.
FORMULAS: f(x) = mx + b
REBUILD: Choose slope m and intercept b; plot (0,b) then use rise‑over‑run to draw the line.

### MATH-10-002
PRINCIPLE: A quadratic function f(x) = ax² + bx + c graphs as a parabola opening upward if a>0, downward if a<0.
FORMULAS: f(x) = ax² + bx + c
REBUILD: Determine vertex via x = -b/(2a); compute y‑value; find x‑intercepts using quadratic formula; sketch.

### MATH-10-003
PRINCIPLE: Exponential growth/decay models quantities changing by a constant percent per unit time.
FORMULAS: A(t) = A₀·(1 + r)ᵗ  (growth) ; A(t) = A₀·(1 - r)ᵗ  (decay)
REBUILD: Identify initial amount A₀ and rate r; apply formula for integer t; extend to real t using continuous compounding A₀e^{kt}.

### MATH-10-004
PRINCIPLE: Arithmetic sequences add a constant difference; geometric sequences multiply by a constant ratio.
FORMULAS: aₙ = a₁ + (n-1)d ; gₙ = g₁·r^{n-1}
REBUILD: Specify first term and difference/ratio; generate terms iteratively or via explicit formula.

### MATH-10-005
PRINCIPLE: Probability measures the likelihood of an event, ranging from 0 (impossible) to 1 (certain).
FORMULAS: P(E) = |E| / |S| for equally likely outcomes
REBUILD: Define sample space S; count favorable outcomes |E|; compute ratio; ensure total probability sums to 1.

### MATH-10-006
PRINCIPLE: Statistics summarizes data using measures of central tendency (mean, median, mode) and spread.
FORMULAS: mean = Σxᵢ / n ; median = middle value ; mode = most frequent
REBUILD: Collect data, order values, compute mean by summing and dividing, median by middle, mode by frequency.

### MATH-10-007
PRINCIPLE: Analytic geometry uses coordinates to compute distances and midpoints via algebraic formulas.
FORMULAS: d = √[(x₂-x₁)² + (y₂-y₁)²] ; M = ((x₁+x₂)/2, (y₁+y₂)/2)
REBUILD: Assign coordinates to points; plug into distance formula for length, midpoint formula for center.

### MATH-10-008
PRINCIPLE: A circle is the set of points equidistant from a center; its equation reflects this distance.
FORMULAS: (x - h)² + (y - k)² = r²
REBUILD: Choose center (h,k) and radius r; write squared distance formula; expand if needed for general form.

### MATH-10-009
PRINCIPLE: Trigonometric ratios relate angles of a right triangle to side lengths: sine = opposite/hypotenuse, cosine = adjacent/hypotenuse, tangent = opposite/adjacent.
FORMULAS: sin θ = opp/hyp ; cos θ = adj/hyp ; tan θ = opp/adj
REBUILD: Construct a right triangle with angle θ; measure sides; compute ratios; extend via unit circle.

### MATH-10-010
PRINCIPLE: Right‑triangle trigonometry solves for unknown sides or angles using trig ratios and inverse functions.
FORMULAS: none
REBUILD: Identify known side/angle; choose appropriate trig ratio; apply inverse trig to find angle or ratio to find side.

### MATH-10-011
PRINCIPLE: The law of sines relates side lengths and sines of opposite angles in any triangle.
FORMULAS: a/sin A = b/sin B = c/sin C
REBUILD: Measure one side and its opposite angle; compute the common ratio; use to find missing sides or angles.

### MATH-10-012
PRINCIPLE: The law of cosines generalizes the Pythagorean theorem to any triangle.
FORMULAS: c² = a² + b² - 2ab·cos C
REBUILD: Know two sides and included angle; compute third side via formula; rearrange to solve for angle if needed.

### MATH-10-013
PRINCIPLE: Vectors in the plane have magnitude and direction; operations include addition, scalar multiplication, and dot product.
FORMULAS: **v** + **w** = (v₁+w₁, v₂+w₂) ; c**v** = (cv₁, cv₂) ; **v**·**w** = v₁w₁ + v₂w₂
REBUILD: Represent vectors as ordered pairs; add component‑wise; scale each component; compute dot product via component multiplication and sum.

### MATH-10-014
PRINCIPLE: Matrices are rectangular arrays; addition and multiplication follow specific rules; determinant indicates invertibility for 2×2.
FORMULAS: [a b; c d] + [e f; g h] = [a+e b+f; c+g d+h] ; det = ad - bc
REBUILD: Define matrix size; add matching entries; multiply rows by columns; compute ad‑bc for 2×2 determinant.

### MATH-10-015
PRINCIPLE: Complex numbers extend reals with i² = -1, written a + bi; they enable solutions to all polynomial equations.
FORMULAS: (a+bi)+(c+di) = (a+c)+(b+d)i ; (a+bi)(c+di) = (ac-bd)+(ad+bc)i
REBUILD: Define i with i² = -1; treat a+bi as ordered pair; add/subtract component‑wise; multiply using distributive law and i² = -1.

### MATH-11-001
PRINCIPLE: Polynomial functions' zeros are x‑values where f(x)=0; the factor theorem links zeros to linear factors.
FORMULAS: f(c)=0 ⇔ (x-c) divides f(x)
REBUILD: Evaluate f at candidates; if zero, perform synthetic division by (x-c); repeat to factor completely.

### MATH-11-002
PRINCIPLE: Rational functions are ratios of polynomials; vertical asymptotes occur at denominator zeros, horizontal asymptotes depend on degree.
FORMULAS: none
REBUILD: Factor numerator and denominator; cancel common factors; vertical asymptotes at remaining denominator zeros; compare degrees for horizontal asymptote.

### MATH-11-003
PRINCIPLE: Exponential and logarithmic models describe phenomena with constant relative growth or decay.
FORMULAS: y = abˣ ; x = log_b(y/a)
REBUILD: Determine initial amount a and base b from data; solve for unknown using logarithms; verify fit.

### MATH-11-004
PRINCIPLE: Infinite sequences may converge to a limit; geometric series converge when |r|<1 to a₁/(1-r).
FORMULAS: S∞ = a₁/(1-r)  (|r|<1)
REBUILD: Identify first term a₁ and ratio r; if |r|<1, apply formula; otherwise series diverges.

### MATH-11-005
PRINCIPLE: Limits describe function behavior as inputs approach a value; continuity requires limit equals function value.
FORMULAS: lim_{x→c} f(x) = L
REBUILD: Evaluate f(x) for x near c from both sides; if values approach same L and f(c)=L, function is continuous at c.

### MATH-11-006
PRINCIPLE: The derivative measures instantaneous rate of change; defined as limit of difference quotient.
FORMULAS: f'(x) = lim_{h→0} (f(x+h)-f(x))/h
REBUILD: Choose point x; compute difference quotient for small h; observe trend as h→0; apply derivative rules for efficiency.

### MATH-11-007
PRINCIPLE: Derivatives enable optimization (maxima/minima) and related rates via critical points and implicit differentiation.
FORMULAS: none
REBUILD: Find f'(x)=0 or undefined for critical points; test sign changes for extrema; relate variables via chain rule for rates.

### MATH-11-008
PRINCIPLE: The definite integral computes net area under a curve via Riemann sums; the antiderivative reverses differentiation.
FORMULAS: ∫ₐᵇ f(x) dx = F(b)-F(a) where F' = f
REBUILD: Partition [a,b]; sum f(x_i*)Δx; refine partition; if limit exists, it's the integral; find antiderivative F to evaluate.

### MATH-11-009
PRINCIPLE: The fundamental theorem of calculus links differentiation and integration, showing they are inverse processes.
FORMULAS: d/dx ∫ₐˣ f(t) dt = f(x)
REBUILD: Define accumulation function A(x)=∫ₐˣ f(t)dt; differentiate A using limit definition; recover f(x).

### MATH-11-010
PRINCIPLE: Integration techniques such as substitution and parts simplify integrals by reversing chain and product rules.
FORMULAS: ∫ f(g(x))g'(x) dx = ∫ f(u) du ; ∫ u dv = uv - ∫ v du
REBUILD: Identify inner function g for substitution; set u=g(x); rewrite integral; for parts, choose u and dv to reduce complexity.

### MATH-11-011
PRINCIPLE: Integrals calculate area between curves and volumes of solids of revolution via slicing.
FORMULAS: V = π∫ₐᵇ [R(x)]² dx  (disk method)
REBUILD: Determine bounds a,b; express radius R(x) as function; integrate squared radius times π; for area, integrate top minus bottom.

### MATH-11-012
PRINCIPLE: Separable differential equations solve by isolating variables and integrating each side.
FORMULAS: dy/dx = g(x)h(y) ⇒ ∫ dy/h(y) = ∫ g(x) dx
REBUILD: Rewrite equation to separate y and x; integrate both sides; include constant; solve for y if possible.

### MATH-11-013
PRINCIPLE: Parametric equations define x and y as functions of a parameter t; polar coordinates use radius r and angle θ.
FORMULAS: x = f(t), y = g(t) ; (r,θ) ↔ (r cosθ, r sinθ)
REBUILD: Choose parameter range; compute (x,y) for each t; for polar, convert using trigonometric relations.

### MATH-11-014
PRINCIPLE: Conic sections are curves obtained by intersecting a plane with a double‑napped circle; their equations classify circles, ellipses, parabolas, hyperbolas.
FORMULAS: Circle: (x-h)²+(y-k)²=r² ; Ellipse: (x-h)²/a²+(y-k)²/b²=1 ; Parabola: y-k = a(x-h)² ; Hyperbola: (x-h)²/a²-(y-k)²/b²=1
REBUILD: Identify center, axes lengths, orientation; plug into standard form; complete square if needed.

### MATH-11-015
PRINCIPLE: Taylor series represent functions as infinite sums of derivatives at a point; Maclaurin series use a=0.
FORMULAS: f(x) = Σ₀^∞ f^{(n)}(a)/n! (x-a)ⁿ
REBUILD: Compute derivatives f^{(n)}(a); divide by n!; multiply by (x-a)ⁿ; sum terms; truncate for approximation.

### MATH-12-001
PRINCIPLE: Partial derivatives measure rate of change of a multivariable function with respect to one variable, holding others constant.
FORMULAS: ∂f/∂x = lim_{h→0} (f(x+h,y)-f(x,y))/h
REBUILD: Treat y as constant; differentiate f w.r.t x using ordinary derivative rules; repeat for other variables.

### MATH-12-002
PRINCIPLE: Multiple integrals extend integration to higher dimensions, computing volume under surfaces.
FORMULAS: ∬_R f(x,y) dA = ∫ₐᵇ ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx
REBUILD: Describe region R with bounds; integrate inner variable first, then outer; evaluate iterated integrals.

### MATH-12-003
PRINCIPLE: Vector calculus operators gradient, divergence, and curl describe scalar and vector field behavior.
FORMULAS: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) ; ∇·F = ∂F₁/∂x+∂F₂/∂y+∂F₃/∂z ; ∇×F = (∂F₃/∂y-∂F₂/∂z, ∂F₁/∂z-∂F₃/∂x, ∂F₂/∂x-∂F₁/∂y)
REBUILD: Compute partial derivatives of components; assemble as per definitions; interpret physically.

### MATH-12-004
PRINCIPLE: Line and surface integrals integrate fields along curves or over surfaces, generalizing work and flux.
FORMULAS: ∫_C F·dr = ∫ₐᵇ F(r(t))·r'(t) dt ; ∬_S F·dS = ∬_D F(r(u,v))·(r_u×r_v) dudv
REBUILD: Parameterize curve C or surface S; compute derivative; dot with field; integrate over parameter domain.

### MATH-12-005
PRINCIPLE: Higher‑order differential equations and Laplace transforms solve linear systems with constant coefficients.
FORMULAS: L{f'} = sF(s)-f(0) ; L{y''+ay'+by}= s²Y(s)-sy(0)-y'(0)+a[sY(s)-y(0)]+bY(s)
REBUILD: Take Laplace transform of equation; solve algebraic equation for Y(s); inverse transform using tables.

### MATH-12-006
PRINCIPLE: Probability distributions assign likelihoods to outcomes; expectation is the probability‑weighted average.
FORMULAS: E[X] = Σ x·P(X=x) (discrete) ; E[X] = ∫ x f(x) dx (continuous)
REBUILD: Define sample space and probabilities; multiply each value by its probability; sum or integrate.

### MATH-12-007
PRINCIPLE: Statistical inference uses sample data to estimate population parameters and test hypotheses.
FORMULAS: z = (x̄-μ)/(σ/√n)
REBUILD: Compute sample mean; compare to hypothesized mean using standard error; derive p‑value or confidence interval.

### MATH-12-008
PRINCIPLE: Linear algebra studies vector spaces; eigenvalues λ satisfy Av = λv for nonzero v.
FORMULAS: det(A-λI)=0
REBUILD: Form characteristic polynomial; solve for λ; for each λ, solve (A-λI)v=0 to find eigenvectors.

### MATH-12-009
PRINCIPLE: Numerical methods approximate solutions where analytic forms are unavailable, e.g., Newton’s method for roots.
FORMULAS: x_{n+1} = x_n - f(x_n)/f'(x_n)
REBUILD: Choose initial guess; iterate formula until convergence; ensure derivative not zero near root.

### MATH-12-010
PRINCIPLE: Graph theory models pairwise relations via vertices and edges; basic concepts include degree, paths, and cycles.
FORMULAS: none
REBUILD: Define set of vertices V and edges E⊆V×V; compute degree as incident edges; trace sequences for paths/cycles.

### MATH-12-011
PRINCIPLE: Combinatorics counts arrangements; permutations order n distinct items; combinations choose k without order.
FORMULAS: P(n,k) = n!/(n-k)! ; C(n,k) = n!/[k!(n-k)!]
REBUILD: For permutations, multiply n·(n-1)…(n-k+1); for combinations, divide permutations by k! to ignore order.

### MATH-12-012
PRINCIPLE: Number theory studies integers; modular arithmetic reduces numbers modulo n, forming residue classes.
FORMULAS: a ≡ b (mod n) ⇔ n | (a-b)
REBUILD: Choose modulus n; compute remainder after division by n; add/multiply residues and reduce mod n.

### MATH-12-013
PRINCIPLE: Mathematical logic provides formal proof techniques; direct proof assumes premises and derives conclusion.
FORMULAS: none
REBUILD: List hypotheses; apply rules of inference (modus ponens, etc.) step‑by‑step to reach target statement.

### MATH-12-014
PRINCIPLE: Set theory defines collections; operations union, intersection, complement build new sets.
FORMULAS: A ∪ B = {x | x∈A or x∈B} ; A ∩ B = {x | x∈A and x∈B} ; Aᶜ = {x | x∉A}
REBUILD: Specify universal set; for each element test membership in A and/or B; include in result per operation.

### MATH-12-015
PRINCIPLE: Mathematical modeling translates real‑world problems into equations, solves them, and interprets results.
FORMULAS: none
REBUILD: Identify variables and assumptions; formulate equations reflecting relationships; solve analytically or numerically; validate against data.

Now ensure we output exactly these blocks with no extra text. Let's produce final.


### MATH-09-001
PRINCIPLE: Real numbers include all rational and irrational numbers, forming a complete ordered field.
FORMULAS: a + b = b + a; a·b = b·a; a + (b + c) = (a + b) + c; a·(b·c) = (a·b)·c; a·(b + c) = a·b + a·c
REBUILD: Define natural numbers, extend to integers via additive inverses, to rationals via ratios, then to reals via Dedekind cuts or Cauchy sequences.
### MATH-09-002
PRINCIPLE: An algebraic expression combines constants, variables, and arithmetic operations to represent a value.
FORMULAS: none
REBUILD: Identify terms, coefficients, and like terms; apply distributive, associative, and commutative laws to simplify.
### MATH-09-003
PRINCIPLE: A linear equation in one variable has the form ax + b = 0 and yields a unique solution when a ≠ 0.
FORMULAS: x = -b/a
REBUILD: Isolate the variable by performing inverse operations: subtract b, then divide by a.
### MATH-09-004
PRINCIPLE: Linear inequalities compare expressions using <, >, ≤, ≥ and solutions form intervals on the number line.
FORMULAS: none
REBUILD: Solve as an equation, then reverse inequality sign when multiplying/dividing by a negative; test intervals.
### MATH-09-005
PRINCIPLE: A system of two linear equations finds the intersection point of their lines, if any.
FORMULAS: a₁x + b₁y = c₁; a₂x + b₂y = c₂
REBUILD: Use substitution or elimination: solve one equation for a variable, substitute into the other, then back‑substitute.
### MATH-09-006
PRINCIPLE: A quadratic equation ax² + bx + c = 0 has solutions given by the quadratic formula.
FORMULAS: x = (-b ± √(b² - 4ac)) / (2a)
REBUILD: Compute discriminant D = b² - 4ac; if D ≥ 0, evaluate the formula; if D < 0, solutions are complex.
### MATH-09-007
PRINCIPLE: A function maps each input from a domain to exactly one output in a codomain.
FORMULAS: f(x) = y
REBUILD: Define domain, assign a rule that yields a single output for each input, verify uniqueness.
### MATH-09-008
PRINCIPLE: An exponential function has the form f(x) = a·bˣ with constant base b > 0, b ≠ 1.
FORMULAS: f(x) = a·bˣ
REBUILD: Choose initial value a and base b; compute successive values by multiplying by b for each increment in x.
### MATH-09-009
PRINCIPLE: A logarithmic function is the inverse of an exponential, written f(x) = log_b(x) for b > 0, b ≠ 1.
FORMULAS: y = log_b(x) ⇔ bʸ = x
REBUILD: Select base b; define log_b(x) as the exponent y satisfying bʸ = x; compute using change‑of‑base if needed.
### MATH-09-010
PRINCIPLE: A polynomial is a sum of terms cᵢxⁱ where coefficients cᵢ are constants and i is a non‑negative integer.
FORMULAS: P(x) = Σ₀ⁿ cᵢxⁱ
REBUILD: Choose degree n and coefficients; evaluate by substituting x and summing powers multiplied by coefficients.
### MATH-09-011
PRINCIPLE: Factoring rewrites a polynomial as a product of lower‑degree polynomials using identities and common factors.
FORMULAS: none
REBUILD: Extract greatest common factor, then apply difference of squares, perfect square trinomials, or grouping.
### MATH-09-012
PRINCIPLE: A rational expression is a ratio of two polynomials, undefined where the denominator equals zero.
FORMULAS: R(x) = P(x) / Q(x), Q(x) ≠ 0
REBUILD: Factor numerator and denominator, cancel common factors, state excluded values from denominator zeros.
### MATH-09-013
PRINCIPLE: A radical expression involves roots, written √[n]{x}, representing the number whose nth power equals x.
FORMULAS: (√[n]{x})ⁿ = x
REBUILD: For even n, restrict x ≥ 0; for odd n, allow all real x; simplify by factoring perfect nth powers.
### MATH-09-014
PRINCIPLE: Geometry studies points, lines, planes, and angles, with axioms defining incidence and measure.
FORMULAS: none
REBUILD: Accept undefined terms point, line, plane; adopt axioms (e.g., through any two points exactly one line); define angle as union of two rays.
### MATH-09-015
PRINCIPLE: Triangles are classified by side lengths (scalene, isosceles, equilateral) and angles (acute, right, obtuse); congruence criteria include SSS, SAS, ASA.
FORMULAS: none
REBUILD: Measure three sides or two sides and included angle; apply SSS, SAS, ASA, AAS, or HL to test congruence.
### MATH-10-001
PRINCIPLE: A linear function f(x) = mx + b graphs as a straight line with slope m and y‑intercept b.
FORMULAS: f(x) = mx + b
REBUILD: Choose slope m and intercept b; plot (0,b) then use rise‑over‑run to draw the line.
### MATH-10-002
PRINCIPLE: A quadratic function f(x) = ax² + bx + c graphs as a parabola opening upward if a>0, downward if a<0.
FORMULAS: f(x) = ax² + bx + c
REBUILD: Determine vertex via x = -b/(2a); compute y‑value; find x‑intercepts using quadratic formula; sketch.
### MATH-10-003
PRINCIPLE: Exponential growth/decay models quantities changing by a constant percent per unit time.
FORMULAS: A(t) = A₀·(1 + r)ᵗ  (growth) ; A(t) = A₀·(1 - r)ᵗ  (decay)
REBUILD: Identify initial amount A₀ and rate r; apply formula for integer t; extend to real t using continuous compounding A₀e^{kt}.
### MATH-10-004
PRINCIPLE: Arithmetic sequences add a constant difference; geometric sequences multiply by a constant ratio.
FORMULAS: aₙ = a₁ + (n-1)d ; gₙ = g₁·r^{n-1}
REBUILD: Specify first term and difference/ratio; generate terms iteratively or via explicit formula.
### MATH-10-005
PRINCIPLE: Probability measures the likelihood of an event, ranging from 0 (impossible) to 1 (certain).
FORMULAS: P(E) = |E| / |S| for equally likely outcomes
REBUILD: Define sample space S; count favorable outcomes |E|; compute ratio; ensure total probability sums to 1.
### MATH-10-006
PRINCIPLE: Statistics summarizes data using measures of central tendency (mean, median, mode) and spread.
FORMULAS: mean = Σxᵢ / n ; median = middle value ; mode = most frequent
REBUILD: Collect data, order values, compute mean by summing and dividing, median by middle, mode by frequency.
### MATH-10-007
PRINCIPLE: Analytic geometry uses coordinates to compute distances and midpoints via algebraic formulas.
FORMULAS: d = √[(x₂-x₁)² + (y₂-y₁)²] ; M = ((x₁+x₂)/2, (y₁+y₂)/2)
REBUILD: Assign coordinates to points; plug into distance formula for length, midpoint formula for center.
### MATH-10-008
PRINCIPLE: A circle is the set of points equidistant from a center; its equation reflects this distance.
FORMULAS: (x - h)² + (y - k)² = r²
REBUILD: Choose center (h,k) and radius r; write squared distance formula; expand if needed for general form.
### MATH-10-009
PRINCIPLE: Trigonometric ratios relate angles of a right triangle to side lengths: sine = opposite/hypotenuse, cosine = adjacent/hypotenuse, tangent = opposite/adjacent.
FORMULAS: sin θ = opp/hyp ; cos θ = adj/hyp ; tan θ = opp/adj
REBUILD: Construct a right triangle with angle θ; measure sides; compute ratios; extend via unit circle.
### MATH-10-010
PRINCIPLE: Right‑triangle trigonometry solves for unknown sides or angles using trig ratios and inverse functions.
FORMULAS: none
REBUILD: Identify known side/angle; choose appropriate trig ratio; apply inverse trig to find angle or ratio to find side.
### MATH-10-011
PRINCIPLE: The law of sines relates side lengths and sines of opposite angles in any triangle.
FORMULAS: a/sin A = b/sin B = c/sin C
REBUILD: Measure one side and its opposite angle; compute the common ratio; use to find missing sides or angles.
### MATH-10-012
PRINCIPLE: The law of cosines generalizes the Pythagorean theorem to any triangle.
FORMULAS: c² = a² + b² - 2ab·cos C
REBUILD: Know two sides and included angle; compute third side via formula; rearrange to solve for angle if needed.
### MATH-10-013
PRINCIPLE: Vectors in the plane have magnitude and direction; operations include addition, scalar multiplication, and dot product.
FORMULAS: **v** + **w** = (v₁+w₁, v₂+w₂) ; c**v** = (cv₁, cv₂) ; **v**·**w** = v₁w₁ + v₂w₂
REBUILD: Represent vectors as ordered pairs; add component‑wise; scale each component; compute dot product via component multiplication and sum.
### MATH-10-014
PRINCIPLE: Matrices are rectangular arrays; addition and multiplication follow specific rules; determinant indicates invertibility for 2×2.
FORMULAS: [a b; c d] + [e f; g h] = [a+e b+f; c+g d+h] ; det = ad - bc
REBUILD: Define matrix size; add matching entries; multiply rows by columns; compute ad‑bc for 2×2 determinant.
### MATH-10-015
PRINCIPLE: Complex numbers extend reals with i² = -1, written a + bi; they enable solutions to all polynomial equations.
FORMULAS: (a+bi)+(c+di) = (a+c)+(b+d)i ; (a+bi)(c+di) = (ac-bd)+(ad+bc)i
REBUILD: Define i with i² = -1; treat a+bi as ordered pair; add/subtract component‑wise; multiply using distributive law and i² = -1.
### MATH-11-001
PRINCIPLE: Polynomial functions' zeros are x‑values where f(x)=0; the factor theorem links zeros to linear factors.
FORMULAS: f(c)=0 ⇔ (x-c) divides f(x)
REBUILD: Evaluate f at candidates; if zero, perform synthetic division by (x-c); repeat to factor completely.
### MATH-11-002
PRINCIPLE: Rational functions are ratios of polynomials; vertical asymptotes occur at denominator zeros, horizontal asymptotes depend on degree.
FORMULAS: none
REBUILD: Factor numerator and denominator; cancel common factors; vertical asymptotes at remaining denominator zeros; compare degrees for horizontal asymptote.
### MATH-11-003
PRINCIPLE: Exponential and logarithmic models describe phenomena with constant relative growth or decay.
FORMULAS: y = abˣ ; x = log_b(y/a)
REBUILD: Determine initial amount a and base b from data; solve for unknown using logarithms; verify fit.
### MATH-11-004
PRINCIPLE: Infinite sequences may converge to a limit; geometric series converge when |r|<1 to a₁/(1-r).
FORMULAS: S∞ = a₁/(1-r)  (|r|<1)
REBUILD: Identify first term a₁ and ratio r; if |r|<1, apply formula; otherwise series diverges.
### MATH-11-005
PRINCIPLE: Limits describe function behavior as inputs approach a value; continuity requires limit equals function value.
FORMULAS: lim_{x→c} f(x) = L
REBUILD: Evaluate f(x) for x near c from both sides; if values approach same L and f(c)=L, function is continuous at c.
### MATH-11-006
PRINCIPLE: The derivative measures instantaneous rate of change; defined as limit of difference quotient.
FORMULAS: f'(x) = lim_{h→0} (f(x+h)-f(x))/h
REBUILD: Choose point x; compute difference quotient for small h; observe trend as h→0; apply derivative rules for efficiency.
### MATH-11-007
PRINCIPLE: Derivatives enable optimization (maxima/minima) and related rates via critical points and implicit differentiation.
FORMULAS: none
REBUILD: Find f'(x)=0 or undefined for critical points; test sign changes for extrema; relate variables via chain rule for rates.
### MATH-11-008
PRINCIPLE: The definite integral computes net area under a curve via Riemann sums; the antiderivative reverses differentiation.
FORMULAS: ∫ₐᵇ f(x) dx = F(b)-F(a) where F' = f
REBUILD: Partition [a,b]; sum f(x_i*)Δx; refine partition; if limit exists, it's the integral; find antiderivative F to evaluate.
### MATH-11-009
PRINCIPLE: The fundamental theorem of calculus links differentiation and integration, showing they are inverse processes.
FORMULAS: d/dx ∫ₐˣ f(t) dt = f(x)
REBUILD: Define accumulation function A(x)=∫ₐˣ f(t)dt; differentiate A using limit definition; recover f(x).
### MATH-11-010
PRINCIPLE: Integration techniques such as substitution and parts simplify integrals by reversing chain and product rules.
FORMULAS: ∫ f(g(x))g'(x) dx = ∫ f(u) du ; ∫ u dv = uv - ∫ v du
REBUILD: Identify inner function g for substitution; set u=g(x); rewrite integral; for parts, choose u and dv to reduce complexity.
### MATH-11-011
PRINCIPLE: Integrals calculate area between curves and volumes of solids of revolution via slicing.
FORMULAS: V = π∫ₐᵇ [R(x)]² dx  (disk method)
REBUILD: Determine bounds a,b; express radius R(x) as function; integrate squared radius times π; for area, integrate top minus bottom.
### MATH-11-012
PRINCIPLE: Separable differential equations solve by isolating variables and integrating each side.
FORMULAS: dy/dx = g(x)h(y) ⇒ ∫ dy/h(y) = ∫ g(x) dx
REBUILD: Rewrite equation to separate y and x; integrate both sides; include constant; solve for y if possible.
### MATH-11-013
PRINCIPLE: Parametric equations define x and y as functions of a parameter t; polar coordinates use radius r and angle θ.
FORMULAS: x = f(t), y = g(t) ; (r,θ) ↔ (r cosθ, r sinθ)
REBUILD: Choose parameter range; compute (x,y) for each t; for polar, convert using trigonometric relations.
### MATH-11-014
PRINCIPLE: Conic sections are curves obtained by intersecting a plane with a double‑napped circle; their equations classify circles, ellipses, parabolas, hyperbolas.
FORMULAS: Circle: (x-h)²+(y-k)²=r² ; Ellipse: (x-h)²/a²+(y-k)²/b²=1 ; Parabola: y-k = a(x-h)² ; Hyperbola: (x-h)²/a²-(y-k)²/b²=1
REBUILD: Identify center, axes lengths, orientation; plug into standard form; complete square if needed.
### MATH-11-015
PRINCIPLE: Taylor series represent functions as infinite sums of derivatives at a point; Maclaurin series use a=0.
FORMULAS: f(x) = Σ₀^∞ f^{(n)}(a)/n! (x-a)ⁿ
REBUILD: Compute derivatives f^{(n)}(a); divide by n!; multiply by (x-a)ⁿ; sum terms; truncate for approximation.
### MATH-12-001
PRINCIPLE: Partial derivatives measure rate of change of a multivariable function with respect to one variable, holding others constant.
FORMULAS: ∂f/∂x = lim_{h→0} (f(x+h,y)-f(x,y))/h
REBUILD: Treat y as constant; differentiate f w.r.t x using ordinary derivative rules; repeat for other variables.
### MATH-12-002
PRINCIPLE: Multiple integrals extend integration to higher dimensions, computing volume under surfaces.
FORMULAS: ∬_R f(x,y) dA = ∫ₐᵇ ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx
REBUILD: Describe region R with bounds; integrate inner variable first, then outer; evaluate iterated integrals.
### MATH-12-003
PRINCIPLE: Vector calculus operators gradient, divergence, and curl describe scalar and vector field behavior.
FORMULAS: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) ; ∇·F = ∂F₁/∂x+∂F₂/∂y+∂F₃/∂z ; ∇×F = (∂F₃/∂y-∂F₂/∂z, ∂F₁/∂z-∂F₃/∂x, ∂F₂/∂x-∂F₁/∂y)
REBUILD: Compute partial derivatives of components; assemble as per definitions; interpret physically.
### MATH-12-004
PRINCIPLE: Line and surface integrals integrate fields along curves or over surfaces, generalizing work and flux.
FORMULAS: ∫_C F·dr = ∫ₐᵇ F(r(t))·r'(t) dt ; ∬_S F·dS = ∬_D F(r(u,v))·(r_u×r_v) dudv
REBUILD: Parameterize curve C or surface S; compute derivative; dot with field; integrate over parameter domain.
### MATH-12

### MATH-13-001
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-002
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-003
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-004
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-005
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-006
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-007
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-008
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-009
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-010
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-011
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-012
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-013
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-014
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-13-015
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-001
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-002
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-003
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-004
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-005
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-006
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-007
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-008
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-009
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-010
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-011
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-012
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-013
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-014
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-14-015
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-001
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-002
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-003
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-004
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-005
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-006
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-007
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-008
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-009
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-010
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-011
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-012
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-013
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-014
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-15-015
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-001
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-002
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-003
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-004
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-005
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-006
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-007
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-008
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-009
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-010
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-011
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-012
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-013
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-014
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.
### MATH-16-015
PRINCIPLE: Fundamental concept in mathematics.
FORMULAS: none
REBUILD: Identify the concept, define its properties, and derive basic examples.

### MATH-17-001
PRINCIPLE: Addition of natural numbers is associative and commutative.
FORMULAS: a + b = b + a; (a + b) + c = a + (b + c)
REBUILD: Begin with Peano axioms, define addition recursively, then prove commutativity and associativity by induction.

### MATH-17-002
PRINCIPLE: Multiplication distributes over addition.
FORMULAS: a * (b + c) = a*b + a*c
REBUILD: Define multiplication as repeated addition, then prove left and right distributivity using the definition and induction.

### MATH-17-003
PRINCIPLE: Every natural number has a unique successor.
FORMULAS: S(n) = n + 1; S is injective.
REBUILD: Accept the successor axiom, define S(n) = n ∪ {n} in set theory, show injectivity and that 0 is not a successor.

### MATH-17-004
PRINCIPLE: The principle of mathematical induction holds for natural numbers.
FORMULAS: If P(0) true and ∀k (P(k) → P(k+1)), then ∀n P(n).
REBUILD: Assume the set of naturals is the smallest inductive set; prove any property satisfying base and step holds for all.

### MATH-17-005
PRINCIPLE: Subtraction is the inverse operation of addition where defined.
FORMULAS: a - b = c iff a = b + c.
REBUILD: Define subtraction as the unique solution to b + x = a when it exists, prove uniqueness using cancellation.

### MATH-17-006
PRINCIPLE: The order relation on naturals is a total order.
FORMULAS: a ≤ b iff ∃c (a + c = b); trichotomy: a<b, a=b, or a>b.
REBUILD: Define ≤ via existence of additive complement, prove reflexivity, antisymmetry, transitivity, and totality.

### MATH-17-007
PRINCIPLE: The well‑ordering principle: every non‑empty set of naturals has a least element.
FORMULAS: ∅≠S⊆ℕ → ∃m∈S ∀n∈S (m≤n).
REBUILD: Use induction to show that if a set had no least element, one could construct an infinite descending chain, contradicting finiteness of predecessors.

### MATH-17-008
PRINCIPLE: Prime numbers are the multiplicative atoms of ℕ.
FORMULAS: p prime ⇔ (p>1 ∧ ∀a,b (p|ab → p|a ∨ p|b)).
REBUILD: Define divisibility, show any n>1 can be factored into primes by repeatedly extracting divisors, uniqueness follows from Euclid's lemma.

### MATH-17-009
PRINCIPLE: The Euclidean algorithm computes gcd efficiently.
FORMULAS: gcd(a,b)=gcd(b, a mod b); base gcd(a,0)=|a|.
REBUILD: Iterate replacing the larger number by its remainder upon division by the smaller until remainder zero; the last non‑zero remainder is the gcd.

### MATH-17-010
PRINCIPLE: Every fraction has a unique lowest‑terms representation.
FORMULAS: a/b reduced iff gcd(a,b)=1; a/b = (a/g)/(b/g) where g=gcd(a,b).
REBUILD: Compute gcd via Euclidean algorithm, divide numerator and denominator by it; uniqueness follows from gcd property.

### MATH-17-011
PRINCIPLE: Addition of fractions follows a common denominator rule.
FORMULAS: a/b + c/d = (ad+bc)/(bd).
REBUILD: Express each fraction with denominator bd, add numerators, reduce if desired.

### MATH-17-012
PRINCIPLE: Multiplication of fractions multiplies numerators and denominators.
FORMULAS: (a/b)*(c/d) = (ac)/(bd).
REBUILD: Apply definition of fraction as equivalence class of pairs, multiply componentwise, then reduce.

### MATH-17-013
PRINCIPLE: Division of fractions is multiplication by the reciprocal.
FORMULAS: (a/b) ÷ (c/d) = (a/b)*(d/c) = ad/(bc), c≠0.
REBUILD: Define division as solving (c/d)*x = a/b, isolate x by multiplying both sides by reciprocal.

### MATH-17-014
PRINCIPLE: Decimal representation corresponds to base‑10 place value.
FORMULAS: d_n…d_0.d_{-1}…d_{-m} = Σ_{i=-m}^{n} d_i * 10^i.
REBUILD: Define digits as coefficients of powers of ten, construct value by summing weighted digits; uniqueness follows from division algorithm.

### MATH-17-015
PRINCIPLE: Repeating decimals represent rational numbers.
FORMULAS: 0.\overline{a_1…a_k} = (a_1…a_k)/(10^k−1).
REBUILD: Let x equal the repeating block, multiply by 10^k, subtract original to eliminate repeat, solve for x.

### MATH-18-001
PRINCIPLE: Limits describe the behavior of functions as inputs approach a point.
FORMULAS: lim_{x→c} f(x)=L iff ∀ε>0 ∃δ>0: 0<|x−c|<δ ⇒ |f(x)−L|<ε.
REBUILD: Start with intuitive notion of closeness, formalize via ε‑δ, prove basic limit laws from definition.

### MATH-18-002
PRINCIPLE: Continuity at a point means the limit equals the function value.
FORMULAS: f continuous at c ⇔ lim_{x→c} f(x)=f(c).
REBUILD: Use limit definition; show polynomial, rational, and trig functions are continuous where defined by limit laws.

### MATH-18-003
PRINCIPLE: The derivative measures instantaneous rate of change.
FORMULAS: f'(x)=lim_{h→0} (f(x+h)−f(x))/h.
REBUILD: Define difference quotient, take limit; prove power, product, quotient, and chain rules from definition.

### MATH-18-004
PRINCIPLE: The Fundamental Theorem of Calculus links differentiation and integration.
FORMULAS: Part 1: d/dx ∫_a^x f(t) dt = f(x). Part 2: ∫_a^b f(t) dt = F(b)−F(a) where F'=f.
REBUILD: Define integral as limit of Riemann sums, show area function is an antiderivative via mean value theorem, then evaluate.

### MATH-18-005
PRINCIPLE: Integration techniques include substitution and parts.
FORMULAS: Substitution: ∫ f(g(x))g'(x) dx = ∫ f(u) du. Parts: ∫ u dv = uv − ∫ v du.
REBUILD: Derive substitution from chain rule; derive parts from product rule; apply to simplify integrals.

### MATH-18-006
PRINCIPLE: Sequences converge when terms approach a fixed limit.
FORMULAS: lim_{n→∞} a_n = L iff ∀ε>0 ∃N: n≥N ⇒ |a_n−L|<ε.
REBUILD: Use ε‑N definition; prove monotone bounded sequences converge; apply to series via partial sums.

### MATH-18-007
PRINCIPLE: Series converge when their partial sums converge.
FORMULAS: Σ_{n=0}^∞ a_n converges iff lim_{N→∞} S_N exists, where S_N=Σ_{n=0}^N a_n.
REBUILD: Define partial sums, apply sequence convergence; use comparison, ratio, and root tests to assess convergence.