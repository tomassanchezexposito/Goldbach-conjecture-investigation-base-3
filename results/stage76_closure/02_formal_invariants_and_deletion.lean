/-
Stage 76 finite invariant proof source. English-only documentation.
STATUS: UNCOMPILED. Lean 4 and Mathlib were not available in the inspected
runtime. This file contains no sorry or new axioms, but is NOT a certificate
of successful elaboration. Run `lake env lean` in an existing Mathlib project.
No analytic theorem or asymptotic prime-deletion norm assertion is formalized.
-/
import Mathlib

namespace Stage76

def C (n : ℤ) : ℤ := 3 + 2 * n
def primeIndex (p : ℤ) : ℤ := (p - 3) / 2

theorem coordinate_index (n : ℤ) : primeIndex (C n) = n := by
  unfold primeIndex C
  omega

theorem coordinate_injective : Function.Injective C := by
  intro a b hab
  unfold C at hab
  omega

theorem odd_coordinate (p : ℤ) (hp : 3 ≤ p) (ho : p % 2 = 1) :
    ∃! a : ℤ, 0 ≤ a ∧ C a = p := by
  refine ⟨(p - 3) / 2, ?_, ?_⟩
  · unfold C
    omega
  · intro a ha
    unfold C at ha
    omega

theorem reflected_positions (a b m : ℤ) :
    C a + C b = 2 * m ↔ a + b = m - 3 := by
  unfold C
  omega

theorem midpoint (m h : ℤ) : (m - h) + (m + h) = 2 * m := by ring

theorem double_symmetry (p q N : ℤ) (hs : p + q = N) :
    N - 2 * p = 2 * q - N ∧ 2 * q - N = q - p := by omega

def Composite (n : ℕ) : Prop := 1 < n ∧ ¬ Nat.Prime n

def HasPair (N : ℕ) : Prop :=
  ∃ p q : ℕ, Nat.Prime p ∧ Nat.Prime q ∧ p < q ∧ p + q = N

def ThreeCase (N : ℕ) : Prop :=
  Nat.Prime (N - 1) ∨ Nat.Prime (N / 2) ∨ HasPair N

def Residual (N : ℕ) : Prop :=
  4 ≤ N ∧ N % 2 = 0 ∧ Composite (N - 1) ∧ Composite (N / 2)

theorem residual_reduction :
    (∀ N : ℕ, 4 ≤ N → N % 2 = 0 → ThreeCase N) ↔
    (∀ N : ℕ, Residual N → HasPair N) := by
  constructor
  · intro hall N hN
    rcases hN with ⟨h4, he, hc1, hc2⟩
    rcases hall N h4 he with h | h | h
    · exact False.elim (hc1.2 h)
    · exact False.elim (hc2.2 h)
    · exact h
  · intro hres N h4 he
    by_cases h1 : Nat.Prime (N - 1)
    · exact Or.inl h1
    by_cases h2 : Nat.Prime (N / 2)
    · exact Or.inr (Or.inl h2)
    · apply Or.inr
      apply Or.inr
      apply hres N
      refine ⟨h4, he, ⟨?_, h1⟩, ⟨?_, h2⟩⟩ <;> omega

def nu (l N : ℕ) : ℕ := if N % l = 0 then 1 else 2

def wheelCount (N : Fin 210) : ℕ :=
  ((Finset.univ : Finset (Fin 210)).filter fun r =>
    Nat.Coprime r.val 210 ∧
      Nat.Coprime ((N.val + 210 - r.val) % 210) 210).card

def wheelProduct (N : Fin 210) : ℕ :=
  (2 - nu 2 N.val) * (3 - nu 3 N.val) *
    (5 - nu 5 N.val) * (7 - nu 7 N.val)

theorem wheel_exact : ∀ N : Fin 210, wheelCount N = wheelProduct N := by
  native_decide

theorem wheel_totient : Nat.totient 210 = 48 := by native_decide

def wheelNormalized (N : Fin 210) : ℚ := 210 * (wheelCount N : ℚ) / 48 ^ 2

theorem wheel_normalization (N : Fin 210) :
    wheelNormalized N = 210 * (wheelProduct N : ℚ) / 48 ^ 2 := by
  unfold wheelNormalized
  rw [wheel_exact N]

theorem noncoprime_totient : Nat.totient (3 * 3) ≠ Nat.totient 3 * Nat.totient 3 := by
  native_decide

theorem counterexample_coefficients :
    (1 / 2 - 1 / 6 : ℚ) = 1 / 3 ∧
    (1 / 2 - 1 / 4 : ℚ) = 1 / 4 ∧
    (1 / 3 - 1 / 4 : ℚ) = 1 / 12 := by norm_num

section Matching
variable {ι : Type*} [Fintype ι]

-- Each index denotes one edge; endpoints of different edges are disjoint.
theorem matching_zero_iff (u v : ι → ℚ)
    (hu : ∀ i, 0 ≤ u i) (hv : ∀ i, 0 ≤ v i) :
    (∑ i, u i * v i) = 0 ↔ ∀ i, u i * v i = 0 := by
  constructor
  · intro hs i
    have hn : ∀ j ∈ (Finset.univ : Finset ι), 0 ≤ u j * v j := by
      intro j _
      exact mul_nonneg (hu j) (hv j)
    exact (Finset.sum_eq_zero_iff_of_nonneg hn).mp hs i (Finset.mem_univ i)
  · intro hz
    exact Finset.sum_eq_zero (fun i _ => hz i)

theorem matching_cost_lower (a b u v : ι → ℚ)
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ i, 0 ≤ b i)
    (hu : ∀ i, 0 ≤ u i ∧ u i ≤ a i)
    (hv : ∀ i, 0 ≤ v i ∧ v i ≤ b i)
    (hz : ∀ i, u i * v i = 0) :
    (∑ i, min (a i) (b i)) ≤ ∑ i, ((a i - u i) + (b i - v i)) := by
  apply Finset.sum_le_sum
  intro i _
  rcases mul_eq_zero.mp (hz i) with hi | hi
  · have hm := min_le_left (a i) (b i)
    have hvb := (hv i).2
    rw [hi]
    linarith
  · have hm := min_le_right (a i) (b i)
    have hua := (hu i).2
    rw [hi]
    linarith

theorem matching_cost_attained (a b : ι → ℚ)
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ i, 0 ≤ b i) :
    ∃ u v : ι → ℚ,
      (∀ i, 0 ≤ u i ∧ u i ≤ a i ∧ 0 ≤ v i ∧ v i ≤ b i) ∧
      (∀ i, u i * v i = 0) ∧
      (∑ i, ((a i - u i) + (b i - v i))) = ∑ i, min (a i) (b i) := by
  classical
  let u : ι → ℚ := fun i => if a i ≤ b i then 0 else a i
  let v : ι → ℚ := fun i => if a i ≤ b i then b i else 0
  refine ⟨u, v, ?_, ?_, ?_⟩
  · intro i
    by_cases h : a i ≤ b i <;> simp [u, v, h, ha i, hb i]
  · intro i
    by_cases h : a i ≤ b i <;> simp [u, v, h]
  · apply Finset.sum_congr rfl
    intro i _
    by_cases h : a i ≤ b i
    · simp [u, v, h, min_eq_left h]
    · have hba : b i ≤ a i := le_of_lt (lt_of_not_ge h)
      simp [u, v, h, min_eq_right hba]
end Matching
end Stage76
