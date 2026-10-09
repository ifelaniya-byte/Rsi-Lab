# BLACK BOX volume: physics
# Restart-civilization knowledge. Quality-filtered.

### PHYS-01-001
PRINCIPLE: Position, velocity, and acceleration describe motion; velocity is derivative of position, acceleration derivative of velocity.
FORMULAS: v = dx/dt, a = dv/dt = d²x/dt²
REBUILD: Measure displacement over time intervals to compute average velocity; differentiate to get instantaneous; repeat for acceleration.

### PHYS-01-002
PRINCIPLE: An object remains at rest or in uniform motion unless acted upon by a net external force.
FORMULAS: ΣF = 0 → constant v
REBUILD: Observe motion of isolated objects; if velocity unchanged, net force zero; apply known forces to test.

### PHYS-01-003
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: ΣF = m a
REBUILD: Apply known force to known mass, measure acceleration; verify proportionality.

### PHYS-01-004
PRINCIPLE: For every action there is an equal and opposite reaction.
FORMULAS: F₁₂ = -F₂₁
REBUILD: Press two objects together; measure forces on each; they are equal magnitude opposite direction.

### PHYS-01-005
PRINCIPLE: Work done by net force equals change in kinetic energy.
FORMULAS: W = ΔK = ½ m v_f² - ½ m v_i²
REBUILD: Apply constant force over distance, compute work; measure speed change; compare.

### PHYS-01-006
PRINCIPLE: Total energy in an isolated system remains constant.
FORMULAS: E_total = K + U = const
REBUILD: Track kinetic and potential energies (e.g., pendulum); sum stays same absent non-conservative forces.

### PHYS-01-007
PRINCIPLE: Total momentum of an isolated system is conserved.
FORMULAS: Σ p_i = const, p = m v
REBUILD: Collide two objects; measure masses and velocities before/after; total momentum unchanged.

### PHYS-01-008
PRINCIPLE: Angular displacement, velocity, and acceleration describe rotational motion.
FORMULAS: ω = dθ/dt, α = dω/dt
REBUILD: Mark a rotating body; measure angle vs time; differentiate to get ω and α.

### PHYS-01-009
PRINCIPLE: Torque causes angular acceleration; angular momentum is conserved without external torque.
FORMULAS: τ = I α, L = I ω, Σ τ_ext = dL/dt
REBUILD: Apply known force at known lever arm to wheel; measure angular acceleration; verify τ = Iα.

### PHYS-01-010
PRINCIPLE: A mass-spring system oscillates with restoring force proportional to displacement.
FORMULAS: F = -k x, ω₀ = sqrt(k/m), x(t)=A cos(ω₀ t+φ)
REBUILD: Attach mass to spring, displace, release; measure period T=2π sqrt(m/k); fit to cosine.

### PHYS-02-001
PRINCIPLE: Temperature indicates thermal equilibrium; Zeroth Law: if A eq B and B eq C then A eq C.
FORMULAS: none
REBUILD: Use thermometer; when two objects give same reading they are in equilibrium; transitivity holds.

### PHYS-02-002
PRINCIPLE: Energy added as heat increases internal energy or does work; First Law.
FORMULAS: ΔU = Q - W
REBUILD: Measure heat input Q (calorimetry) and work done W (e.g., piston); compute ΔU via temperature change.

### PHYS-02-003
PRINCIPLE: Internal energy of ideal gas depends only on temperature.
FORMULAS: U = (f/2) n R T, f degrees of freedom
REBUILD: Measure temperature change at constant volume; infer ΔU = n C_v ΔT.

### PHYS-02-004
PRINCIPLE: Heat transfers via conduction, convection, radiation; rates given by respective laws.
FORMULAS: Cond: Q/t = k A ΔT / d; Conv: Q/t = h A ΔT; Rad: Q/t = ε σ A (T⁴ - T_s⁴)
REBUILD: Set up slab, measure temperature gradient; compute k; repeat for fluid flow and radiative exchange.

### PHYS-02-005
PRINCIPLE: Entropy of isolated system never decreases; Second Law.
FORMULAS: ΔS ≥ ∫ δQ_rev / T
REBUILD: Allow heat flow between hot and cold bodies; compute entropy change; total ΔS ≥ 0.

### PHYS-02-006
PRINCIPLE: Carnot engine sets max efficiency for heat engines operating between two temperatures.
FORMULAS: η_max = 1 - T_c/T_h
REBUILD: Operate reversible cycle (isothermal/adiabatic) between reservoirs; measure work output vs heat input; ratio approaches formula.

### PHYS-02-007
PRINCIPLE: Ideal gas relates pressure, volume, temperature, and amount.
FORMULAS: p V = n R T
REBUILD: Measure p, V, T for known n; verify proportionality constant R.

### PHYS-02-008
PRINCIPLE: Gas pressure arises from molecular collisions; average kinetic energy proportional to temperature.
FORMULAS: (1/2) m ⟨v²⟩ = (3/2) k_B T
REBUILD: Measure pressure and temperature; infer average speed via kinetic theory; compare with effusion rates.

### PHYS-02-009
PRINCIPLE: Phase transitions occur at constant temperature; latent heat quantifies energy absorbed/released.
FORMULAS: Q = m L (L latent heat)
REBUILD: Heat substance at melting point; measure energy input per mass to melt; equals L_f.

### PHYS-02-010
PRINCIPLE: Thermodynamic potentials (U, H, F, G) encode equilibrium conditions for different constraints.
FORMULAS: H = U + pV, F = U - TS, G = H - TS
REBUILD: For constant T,p processes, minimize G; measure equilibrium composition; verify dG=0.

### PHYS-03-001
PRINCIPLE: Electric charge is quantized and conserved; like charges repel, opposites attract.
FORMULAS: Q = n e, e = 1.602×10⁻¹⁹ C
REBUILD: Rub objects; measure attraction/repulsion with electroscope; count electrons via Millikan oil drop.

### PHYS-03-002
PRINCIPLE: Force between point charges follows inverse-square law.
FORMULAS: F = k_e |q₁ q₂| / r², k_e = 1/(4π ε₀)
REBUILD: Use torsion balance; measure force vs distance for known charges; fit 1/r².

### PHYS-03-003
PRINCIPLE: Electric field E defines force per unit charge; superposition holds.
FORMULAS: E = F/q, E_total = Σ E_i
REBUILD: Place test charge; measure force; divide by q to get E; map around known charge distribution.

### PHYS-03-004
PRINCIPLE: Electric flux through closed surface equals enclosed charge over ε₀ (Gauss's Law).
FORMULAS: ∮ E·dA = Q_enc / ε₀
REBUILD: Surround charge with spherical detector; integrate normal component of E; equals Q/ε₀.

### PHYS-03-005
PRINCIPLE: Electric potential V is potential energy per charge; relates to E via gradient.
FORMULAS: V = U/q, E = -∇V, ΔV = -∫ E·dl
REBUILD: Move test charge in field; measure work done; compute ΔV; compare with line integral of E.

### PHYS-03-006
PRINCIPLE: Capacitance C stores charge per voltage; for parallel plates C = ε₀ A/d.
FORMULAS: Q = C V, C = ε₀ A/d (vac)
REBUILD: Build parallel plates; measure charge vs voltage; slope gives C; vary A,d to test formula.

### PHYS-03-007
PRINCIPLE: Current I is rate of charge flow; resistance R relates V and I via Ohm's law (ohmic).
FORMULAS: I = dQ/dt, V = I R
REBUILD: Apply known voltage; measure current; compute R; repeat for different materials.

### PHYS-03-008
PRINCIPLE: For ohmic conductors, voltage proportional to current with constant resistance.
FORMULAS: V = I R
REBUILD: Plot V vs I; slope gives R; verify linearity.

### PHYS-03-009
PRINCIPLE: Sum of currents entering junction equals sum leaving; sum of voltage drops around loop zero.
FORMULAS: Σ I_in = Σ I_out (KCL), Σ V = 0 (KVL)
REBUILD: Assemble circuit with ammeters/voltmeters; verify conservation at nodes and loops.

### PHYS-03-010
PRINCIPLE: Moving charges produce magnetic field B; force on charge q moving with v is F = q v × B.
FORMULAS: B from current: B = μ₀ I / (2π r) (long wire); F = q v B sinθ
REBUILD: Run current through wire; deflect compass; measure deflection vs I and distance; use Lorentz force on electron beam.

### PHYS-04-001
PRINCIPLE: Waves propagate disturbances; satisfy wave equation ∂²y/∂t² = v² ∂²y/∂x².
FORMULAS: ∂²y/∂t² = v² ∂²y/∂x²
REBUILD: Pulse a string; record shape vs time; fit to wave equation to extract speed v.

### PHYS-04-002
PRINCIPLE: When waves overlap, resultant displacement is sum of individual displacements (superposition).
FORMULAS: y_total = Σ y_i
REBUILD: Send two pulses through medium; measure combined displacement; verify additive.

### PHYS-04-003
PRINCIPLE: Standing waves form when two identical waves travel opposite directions; nodes spaced λ/2.
FORMULAS: y = 2A sin(kx) cos(ωt), λ = 2L/n for fixed ends
REBUILD: Pluck string; observe stationary pattern; measure node spacing; infer wavelength and mode number.

### PHYS-04-004
PRINCIPLE: Observed frequency shifts when source or observer moves relative to medium (Doppler effect).
FORMULAS: f' = f (v ± v_o)/(v ∓ v_s)
REBUILD: Move speaker toward microphone; measure frequency shift; compare with formula using speed of sound.

### PHYS-04-005
PRINCIPLE: Interference intensity depends on phase difference; constructive when Δφ = 2π m.
FORMULAS: I = I₁ + I₂ + 2√(I₁ I₂) cos Δφ
REBUILD: Split laser beam; recombine with variable path difference; record fringes; shift corresponds to Δφ.

### PHYS-04-006
PRINCIPLE: Diffraction bending occurs when wave encounters obstacle comparable to wavelength; angular spread ~ λ/a.
FORMULAS: sin θ = m λ / a (slit), θ ≈ 1.22 λ/D (circular aperture)
REBUILD: Shine laser on narrow slit; measure diffraction pattern width; vary slit width; verify inverse relation.

### PHYS-04-007
PRINCIPLE: Polarization selects electric field orientation; Malus's law gives transmitted intensity.
FORMULAS: I = I₀ cos² θ
REBUILD: Pass polarized light through rotating analyzer; measure intensity vs angle; fit cos².

### PHYS-04-008
PRINCIPLE: Refraction at interface obeys Snell's law; n₁ sinθ₁ = n₂ sinθ₂.
FORMULAS: n₁ sinθ₁ = n₂ sinθ₂
REBUILD: Shine light from air into water; measure incident and refracted angles; compute ratio of sines equals index ratio.

### PHYS-04-009
PRINCIPLE: Lenses and mirrors form images via geometric optics; thin lens equation relates distances.
FORMULAS: 1/f = 1/do + 1/di, M = -di/do
REBUILD: Place object at known distance from lens; locate image; measure distances; verify lens formula.

### PHYS-04-010
PRINCIPLE: Thin-film interference produces colors depending on thickness and refractive index.
FORMULAS: Constructive: 2nt = (m+½)λ (for phase shift), Destructive: 2nt = mλ
REBUILD: Spread oil on water; observe colors; measure thickness via interferometer; match to wavelengths.

### PHYS-05-001
PRINCIPLE: Light ejects electrons from metal if photon energy exceeds work function (photoelectric effect).
FORMULAS: K_max = h f - φ
REBUILD: Shine UV on metal; measure kinetic energy of emitted electrons vs frequency; linear fit gives h and φ.

### PHYS-05-002
PRINCIPLE: Electrons occupy discrete orbits; angular momentum quantized in units of ħ.
FORMULAS: L = n ħ, r_n = n² a₀, E_n = -13.6 eV / n²
REBUILD: Excite hydrogen gas; measure emitted wavelengths; fit to Rydberg formula; infer n levels.

### PHYS-05-003
PRINCIPLE: Quantum state evolves via Schrödinger equation; stationary states satisfy Hψ = Eψ.
FORMULAS: iħ ∂ψ/∂t = Ĥ ψ, Ĥ = -(ħ²/2m)∇² + V
REBUILD: Solve for particle in box numerically; compute energy levels; compare with spectroscopy.

### PHYS-05-004
PRINCIPLE: Certain pairs of observables cannot be simultaneously known beyond ħ/2 limit.
FORMULAS: Δx Δp ≥ ħ/2
REBUILD: Prepare many identical particles; measure position spread and momentum spread; product ≥ ħ/2.

### PHYS-05-005
PRINCIPLE: Particles can penetrate classically forbidden barriers with exponential probability.
FORMULAS: T ≈ exp(-2 κ L), κ = sqrt(2m(V₀-E))/ħ
REBUILD: Send electrons toward thin insulator; measure transmission vs barrier width; fit exponential.

### PHYS-05-006
PRINCIPLE: Laws of physics are same in all inertial frames; speed of light constant c.
FORMULAS: None (postulates)
REBUILD: Measure light speed in moving lab; find invariant; test time dilation via muon decay.

### PHYS-05-007
PRINCIPLE: Moving clocks run slow by factor γ.
FORMULAS: Δt' = γ Δt, γ = 1/√(1 - v²/c²)
REBUILD: Fly atomic clocks on airplanes; compare with ground clocks; elapsed time matches prediction.

### PHYS-05-008
PRINCIPLE: Moving lengths contract along motion direction by factor γ.
FORMULAS: L' = L / γ
REBUILD: Measure distance between simultaneous events in moving frame using light signals; observe contraction.

### PHYS-05-009
PRINCIPLE: Mass and energy are equivalent; rest energy E₀ = mc².
FORMULAS: E = mc²
REBUILD: Measure mass defect in nuclear reactions; compute released energy; matches Δm c².

### PHYS-05-010
PRINCIPLE: Nuclei bind nucleons; binding energy per nucleon peaks near iron.
FORMULAS: B = (Z m_p + N m_n - M_nuc) c²
REBUILD: Measure masses of isotopes; compute mass defect; convert to energy; plot vs A.

### PHYS-06-001
PRINCIPLE: Every mass attracts every other mass with force proportional to product and inverse square of distance.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure acceleration of test mass near known mass; compute G; verify inverse-square by varying r.

### PHYS-06-002
PRINCIPLE: Orbits under central inverse-square force are conic sections; closed orbits are ellipses.
FORMULAS: r = a(1 - e²) / (1 + e cos θ)
REBUILD: Track planet position vs time; fit to ellipse; verify Kepler's laws.

### PHYS-06-003
PRINCIPLE: Planets sweep equal areas in equal times; orbital period squared proportional to semi-major axis cubed.
FORMULAS: T² = (4π²/GM) a³
REBUILD: Measure orbital period and radius for moons; compute constant; confirm across systems.

### PHYS-06-004
PRINCIPLE: Gravitational potential energy of two masses is -G m₁ m₂ / r.
FORMULAS: U = - G m₁ m₂ / r
REBUILD: Separate two masses; measure work needed to pull apart; matches potential difference.

### PHYS-06-005
PRINCIPLE: Tidal forces arise from differential gravity across extended bodies.
FORMULAS: a_tidal ≈ 2 G M r / d³ (for separation r)
REBUILD: Measure ocean bulge height vs moon distance; infer scaling.

### PHYS-06-006
PRINCIPLE: Black hole event horizon radius where escape speed equals c.
FORMULAS: r_s = 2 G M / c²
REBUILD: Observe stellar orbits around invisible massive object; compute radius from velocity; compare to Schwarzschild.

### PHYS-06-007
PRINCIPLE: Universe expands uniformly; recession velocity proportional to distance (Hubble's law).
FORMULAS: v = H₀ d
REBUILD: Measure redshift of galaxies; convert to velocity; plot vs distance; slope gives H₀.

### PHYS-06-008
PRINCIPLE: Cosmic microwave background is blackbody radiation from early universe; temperature ~2.73 K.
FORMULAS: None (observational)
REBUILD: Point microwave antenna at sky; measure spectrum; fit Planck curve; obtain T≈2.73 K.

### PHYS-06-009
PRINCIPLE: Density fluctuations seeded large-scale structure; power spectrum predicts galaxy clustering.
FORMULAS: P(k) ∝ kⁿ T²(k) (transfer function)
REBUILD: Survey galaxy positions; compute two-point correlation; match to ΛCDM predictions.

### PHYS-06-010
PRINCIPLE: Gravitational lensing bends light; deflection angle α = 4GM/(c² b) for point mass.
FORMULAS: α = 4 G M / (c² b)
REBUILD: Observe background star behind massive object; measure angular shift; verify dependence on mass and impact parameter.

### PHYS-07-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-07-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-07-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-07-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-07-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-07-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-07-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-07-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-07-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-07-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-08-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-08-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-08-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-08-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-08-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-08-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-08-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-08-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-08-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-08-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-09-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-09-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-09-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-09-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-09-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-09-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-09-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-09-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-09-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-09-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-10-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-10-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-10-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-10-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-10-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-10-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-10-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-10-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-10-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-10-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-11-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-11-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-11-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-11-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-11-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-11-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-11-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-11-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-11-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-11-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-12-001
PRINCIPLE: Net force equals mass times acceleration.
FORMULAS: F = ma
REBUILD: Measure mass and acceleration; compute force; verify with applied force.

### PHYS-12-002
PRINCIPLE: Momentum is mass times velocity.
FORMULAS: p = mv
REBUILD: Measure mass and velocity; calculate momentum; compare before/after interactions.

### PHYS-12-003
PRINCIPLE: Kinetic energy of a moving object equals half mass times velocity squared.
FORMULAS: E = ½ mv²
REBUILD: Determine mass and speed; compute kinetic energy; check energy changes.

### PHYS-12-004
PRINCIPLE: Gravitational potential energy near Earth’s surface equals mass times gravity times height.
FORMULAS: E = mgh
REBUILD: Measure mass, height; use g≈9.81 m/s²; compute potential energy.

### PHYS-12-005
PRINCIPLE: Newton’s law of universal gravitation gives force between two masses.
FORMULAS: F = G m₁ m₂ / r²
REBUILD: Measure masses and separation; compute force; compare with observed attraction.

### PHYS-12-006
PRINCIPLE: Wave speed equals frequency times wavelength.
FORMULAS: v = f λ
REBUILD: Measure frequency and wavelength; compute speed; validate with timing.

### PHYS-12-007
PRINCIPLE: Voltage across a resistor equals current times resistance (Ohm’s law).
FORMULAS: V = I R
REBUILD: Apply known current; measure voltage; confirm proportionality.

### PHYS-12-008
PRINCIPLE: Electrical power equals voltage times current.
FORMULAS: P = I V
REBUILD: Measure voltage and current; compute power; check against energy usage.

### PHYS-12-009
PRINCIPLE: Heat transferred equals mass times specific heat times temperature change.
FORMULAS: Q = m c ΔT
REBUILD: Measure mass, temperature change; use known c; compute heat; verify.

### PHYS-12-010
PRINCIPLE: Entropy of an ideal gas relates to Boltzmann constant and microstates.
FORMULAS: S = k ln W
REBUILD: Count accessible microstates; compute S; compare with thermodynamic measurements.

### PHYS-13-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-13-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-14-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-15-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-16-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-17-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-001
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-002
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-003
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-004
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-005
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-006
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-007
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-008
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-009
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.
### PHYS-18-010
PRINCIPLE: Fundamental concept of physics.
FORMULAS: none
REBUILD: Observe phenomenon, quantify variables, derive relation.

### PHYS-02-011
PRINCIPLE: Kinematics describes motion through position, velocity, and acceleration as functions of time.
FORMULAS: v = dx/dt, a = dv/dt, x = x₀ + v₀t + ½at², v = v₀ + at, v² = v₀² + 2a(x−x₀)
REBUILD: Measure displacement vs. time, compute slopes for velocity and acceleration; apply equations to predict future motion.

### PHYS-02-012
PRINCIPLE: Newton's First Law states that an object remains at rest or in uniform motion unless acted upon by a net external force.
FORMULAS: ΣF = 0 ⇒ a = 0
REBUILD: Observe an object on a frictionless surface; note constant velocity when no push/pull is applied.

### PHYS-02-013
PRINCIPLE: Newton's Second Law relates net force to mass and acceleration: ΣF = ma.
FORMULAS: ΣF⃗ = m a⃗
REBUILD: Apply known forces to a cart, measure acceleration, verify proportionality to force and inverse to mass.

### PHYS-02-014
PRINCIPLE: Newton's Third Law asserts that forces occur in equal‑and‑opposite pairs acting on different bodies.
FORMULAS: F₁₂ = −F₂₁
REBUILD: Press two carts together; measure equal compression forces on each via force sensors.

### PHYS-02-015
PRINCIPLE: Free‑body diagrams isolate all external forces on a body to apply Newton’s laws systematically.
FORMULAS: none
REBUILD: Sketch the object, label weight, normal, friction, tension, then set ΣF = ma in each axis.

### PHYS-02-016
PRINCIPLE: Work done by a force equals the integral of force dot displacement; the work‑energy theorem links work to kinetic‑energy change.
FORMULAS: W = ∫F·dx, ΔK = W
REBUILD: Pull a block with a known force over a measured distance; compute work and compare to speed change.

### PHYS-02-017
PRINCIPLE: Energy conservation states that total mechanical energy (K+U) remains constant when only conservative forces act.
FORMULAS: K = ½mv², U_g = mgh, U_s = ½kx², E = K + U = const
REBUILD: Release a mass from height h, measure speed at bottom; verify mgh = ½mv².

### PHYS-02-018
PRINCIPLE: Power is the rate at which work is done or energy transferred.
FORMULAS: P = dW/dt = F·v
REBUILD: Lift a weight at constant speed; compute force×velocity and compare to measured energy/time.

### PHYS-02-019
PRINCIPLE: Linear momentum p = mv is conserved in isolated systems; impulse equals change in momentum.
FORMULAS: p = mv, J = ∫F dt = Δp
REBUILD: Collide two gliders on an air track; measure masses and velocities before/after to verify Σp constant.

### PHYS-02-020
PRINCIPLE: Collisions conserve momentum; kinetic energy is conserved only in elastic collisions.
FORMULAS: m₁v₁i + m₂v₂i = m₁v₁f + m₂v₂f; ½m₁v₁i²+½m₂v₂i² = ½m₁v₁f²+½m₂v₂f² (elastic)
REBUILD: Perform cart collisions with varying springiness; record speeds and test both conservation laws.

### PHYS-03-011
PRINCIPLE: Temperature quantifies the average kinetic energy of particles; thermal equilibrium occurs when temperatures equalize.
FORMULAS: ⟨E_k⟩ = (3/2)k_B T (ideal monatomic gas)
REBUILD: Mix two water samples at different temps; measure final common temperature after equilibrium.

### PHYS-03-012
PRINCIPLE: The ideal gas law relates pressure, volume, temperature, and mole number for dilute gases.
FORMULAS: PV = nRT
REBUILD: Measure P, V, T of a sealed syringe with known n; verify proportionality.

### PHYS-03-013
PRINCIPLE: The first law of thermodynamics states that energy change equals heat added minus work done by the system.
FORMULAS: ΔU = Q − W
REBUILD: Heat a gas in a piston, measure temperature rise (ΔU) and work (PΔV); confirm Q = ΔU + W.

### PHYS-03-014
PRINCIPLE: Specific heat c relates heat transfer to temperature change: Q = mcΔT.
FORMULAS: Q = mcΔT
REBUILD: Supply known electrical energy to a metal block, measure ΔT, compute c and compare to tabulated values.

### PHYS-03-015
PRINCIPLE: Latent heat L governs energy absorbed/released during phase change without temperature change.
FORMULAS: Q = mL
REBUILD: Melt ice at 0°C using a heater; measure energy input and mass melted to determine L_f.

### PHYS-03-016
PRINCIPLE: Heat transfer occurs via conduction (Fourier), convection (Newton), and radiation (Stefan‑Boltzmann).
FORMULAS: Q_cond = kAΔT/L, Q_conv = hAΔT, Q_rad = εσA(T⁴−T₀⁴)
REBUILD: Conduct a metal rod experiment, measure temperature gradient to find k; use a heated plate to find h; measure emitted power vs T⁴ for ε.

### PHYS-03-017
PRINCIPLE: The second law introduces entropy S, stating that for any spontaneous process ΔS_univ ≥ 0.
FORMULAS: dS = δQ_rev/T, ΔS = ∫δQ_rev/T
REBUILD: Mix hot and cold water; compute entropy change of each and show total increase.

### PHYS-03-018
PRINCIPLE: A Carnot engine operating between two reservoirs achieves maximal efficiency η = 1−T_c/T_h.
FORMULAS: η = 1 − T_c/T_h
REBUILD: Model a reversible cycle with ideal gas; calculate work output and heat inputs to verify η.

### PHYS-03-019
PRINCIPLE: Ideal gases undergo distinct quasi‑static processes: isothermal (T const), adiabatic (Q=0), isobaric (P const), isochoric (V const).
FORMULAS: Isothermal: PV = const; Adiabatic: PV^γ = const; Isobaric: V/T = const; Isochoric: P/T = const
REBUILD: Perform each process on a piston‑cylinder apparatus, measure P,V,T and confirm corresponding relations.

### PHYS-03-020
PRINCIPLE: Statistical mechanics links microscopic states to macroscopic entropy via S = k_B ln Ω.
FORMULAS: S = k_B ln Ω
REBUILD: Count microstates of two‑state spins (N particles) for given energy; compute S and compare to thermodynamic entropy.

### PHYS-04-011
PRINCIPLE: Electric charge is quantized; Coulomb’s law gives the force between two point charges.
FORMULAS: F = k_e |q₁q₂|/r², k_e = 1/(4πε₀)
REBUILD: Measure force between charged spheres at known distances using a torsion balance; verify inverse‑square law.

### PHYS-04-012
PRINCIPLE: The electric field E defines force per unit charge: F = qE.
FORMULAS: E = F/q, E_point = k_e q/r² r̂
REBUILD: Place a test charge near a known charge, measure deflection, infer E magnitude and direction.

### PHYS-04-013
PRINCIPLE: Gauss’s law relates electric flux through a closed surface to enclosed charge: Φ_E = Q_enc/ε₀.
FORMULAS: Φ_E = ∮E·dA = Q_enc/ε₀
REBUILD: Measure flux through a spherical shell around a point charge using field probes; confirm Q_enc/ε₀.

### PHYS-04-014
PRINCIPLE: Electric potential V is potential energy per unit charge; relates to field via E = −∇V.
FORMULAS: V = U/q, V_point = k_e q/r, E = −∇V
REBUILD: Move a test charge in a known field, measure work done, compute ΔV and compare to −∫E·dl.

### PHYS-04-015
PRINCIPLE: Capacitance C stores charge per voltage: Q = CV; for parallel plates C = ε₀A/d.
FORMULAS: C = Q/V, C_parallel = ε₀A/d
REBUILD: Build a parallel‑plate capacitor, measure charge vs voltage with a voltmeter and electrometer, determine C.

### PHYS-04-016
PRINCIPLE: Electric current I is charge flow rate; Ohm’s law states V = IR for ohmic conductors.
FORMULAS: I = dQ/dt, V = IR
REBUILD: Apply known voltage to a resistor, measure current; verify linear V‑I relationship.

### PHYS-04-017
PRINCIPLE: Kirchhoff’s laws govern DC circuits: junction rule (ΣI_in = ΣI_out) and loop rule (ΣV = 0).
FORMULAS: ΣI = 0 (junction), ΣV = 0 (loop)
REBUILD: Assemble a multi‑loop circuit, measure currents and voltages; check both laws hold within error.

### PHYS-04-018
PRINCIPLE: A magnetic field B exerts a force on moving charges: F = qv×B (Lorentz force).
FORMULAS: F = q v × B
REBUILD: Shoot electrons through a uniform B field, measure deflection radius r = mv/(qB).

### PHYS-04-019
PRINCIPLE: The Biot‑Savart law gives B from a current element; Ampere’s law links ∮B·dl to μ₀I_enc.
FORMULAS: dB = (μ₀/4π) I dl×r̂/r², ∮B·dl = μ₀ I_enc
REBUILD: Measure B around a long straight wire with a Hall probe; verify B = μ₀I/(2πr).

### PHYS-04-020
PRINCIPLE: Faraday’s law states induced emf equals −dΦ_B/dt; Lenz’s law gives its direction to oppose flux change.
FORMULAS: ε = −dΦ_B/dt, Φ_B = ∫B·dA
REBUILD: Move a magnet through a coil, measure induced voltage; compare magnitude to rate of flux change.

### PHYS-05-011
PRINCIPLE: Special relativity rests on two postulates: laws of physics are identical in all inertial frames, and light speed c is constant.
FORMULAS: none
REBUILD: Measure light speed in moving apparatus (Michelson‑Morley) to confirm invariance; deduce relativity principles.

### PHYS-05-012
PRINCIPLE: Time dilation and length contraction arise from Lorentz transformations: Δt = γΔτ, L = L₀/γ.
FORMULAS: γ = 1/√(1−v²/c²), Δt = γΔτ, L = L₀/γ
REBUILD: Observe muon decay rates at high altitude vs surface; confirm increased lifetime due to γ.

### PHYS-05-013
PRINCIPLE: Relativistic momentum and energy unify as p = γmv, E = γmc², with invariant E²−(pc)² = (m₀c²)².
FORMULAS: p = γmv, E = γmc², E² = (pc)² + (m₀c²)²
REBUILD: Accelerate electrons in a linac, measure momentum via magnetic rigidity and energy via calorimetry; verify relations.

### PHYS-05-014
PRINCIPLE: Wave‑particle duality assigns wavelength λ = h/p to matter (de Broglie).
FORMULAS: λ = h/p
REBUILD: Diffract electrons through a crystal lattice, measure diffraction peaks, compute λ and compare to h/p.

### PHYS-05-015
PRINCIPLE: Heisenberg’s uncertainty principle limits simultaneous knowledge of position and momentum: ΔxΔp ≥ ħ/2.
FORMULAS: Δx Δp ≥ ħ/2
REBUILD: Pass electrons through a narrow slit, measure spread in position and resulting momentum distribution; verify product ≥ ħ/2.

### PHYS-05-016
PRINCIPLE: The time‑independent Schrödinger equation determines stationary states: Ĥψ = Eψ.
FORMULAS: Ĥψ = Eψ, Ĥ = −(ħ²/2m)∇² + V
REBUILD: Solve for particle in a box numerically; compute allowed energies E_n = n²π²ħ²/(2mL²) and compare to spectral lines.

### PHYS-05-017
PRINCIPLE: Quantum states form a Hilbert space; superposition allows linear combination of basis states.
FORMULAS: |ψ⟩ = Σ c_n |n⟩, Σ|c_n|² = 1
REBUILD: Prepare a spin‑½ system in superposition via RF pulse; measure probabilities in σ_z basis to confirm |c_↑|²+|c_↓|²=1.

### PHYS-05-018
PRINCIPLE: Measurement collapses the wavefunction to an eigenstate of the observable, with probability given by Born rule.
FORMULAS: P(a) = |⟨a|ψ⟩|²
REBUILD: Perform successive spin measurements; after σ_z=+ outcome, subsequent σ_x measurement yields 50/50 outcomes.

### PHYS-05-019
PRINCIPLE: Atomic energy levels arise from quantized electron orbits; Bohr model gives E_n = −13.6 eV/n².
FORMULAS: E_n = −(m_e e⁴)/(8ε₀²h²) · 1/n² = −13.6 eV/n²
REBUILD: Excite hydrogen gas, record emission spectrum; compute wavelengths via ΔE = hc/λ and match to Bohr formula.

### PHYS-05-020
PRINCIPLE: Nuclear binding energy B = Δm c² explains fission/fusion energy release; semi‑empirical mass formula approximates B.
FORMULAS: B = (Zm_p+Nm_n−M_nuc)c²
REBUILD: Measure masses of reactants and products in D‑T fusion; compute mass defect and compare to released 17.6 MeV.