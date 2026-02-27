import random
from collections import defaultdict

class MashingGenerator:
    def __init__(self, sample_text):
        self.sample_text = sample_text
        self.chain = self._build_markov_chain(sample_text)
        
    def _build_markov_chain(self, text):
        """
        Build a first-order Markov chain: records all characters that follow 
        a specific character. This naturally preserves the character frequency 
        and your specific finger-alternating combinations (the "muscle memory").
        """
        chain = defaultdict(list)
        for i in range(len(text) - 1):
            current_char = text[i]
            next_char = text[i+1]
            chain[current_char].append(next_char)
        return chain

    def generate(self, length=150):
        """Generate a spoofed input sequence of the specified length."""
        # Randomly select a starting character from the sample data
        current_char = random.choice(self.sample_text)
        result = [current_char]
        
        for _ in range(length - 1):
            # If the current character has no subsequent characters in the training data 
            # (e.g., the very last character of the sample), pick a new random starting point 
            # to prevent dead ends.
            if current_char not in self.chain or not self.chain[current_char]:
                current_char = random.choice(list(self.chain.keys()))
                
            # Randomly choose the next character based on the Markov chain's weighted probabilities
            next_char = random.choice(self.chain[current_char])
            result.append(next_char)
            current_char = next_char
            
        return "".join(result)

# ==========================================
# Your raw data (used to train the model)
# ==========================================

# Pattern 1: Index/Middle finger hover flow (center-heavy, left-right alternating)
pattern_1_data = "Vdjbdhdhdhgdhdgdhnehdbdhenxhbdgfkwgduwkudhbwbjxghwkxgebxbuebxhnwvxywbhxyhwgxgwhxhjebxywnxhenxfunwkckwnvckwixhskcjhannxuwnvyxksgcuwkbxhwnxgejzkgbfhuwkgdhdjanvdgivehdhejbdbsjhfhdnkebehzhbrgxysjxjskwnhxhr"

# Pattern 2: Thumb grip flow (wide spans, fan-shaped sweeps, includes spacebar)
pattern_2_data = "bxhebxgbsgxjwgxhwhxghedhhebxhnshdhchhehchsnchejhdhdhejsbchejbxhejzhrhwujxhwjbzjwmchwljchwkxnejakwjhxjwjfhqkhxjqkdruksbchwjhdbdkajhfjwhchnwhxjebchjehzhejxyejwbchjwhchwjxhejkqkncnwoqcukwokcjwojxjsoebbcbrjdcbbdr dhjebdhenx"

# ==========================================
# Instantiate and generate test data
# ==========================================

generator_1 = MashingGenerator(pattern_1_data)
generator_2 = MashingGenerator(pattern_2_data)

print("=== Generated Pattern 1 (Simulated Index/Middle Finger Flow) ===")
fake_pattern_1 = generator_1.generate(length=180)
print(fake_pattern_1)
print("\n" + "-"*50 + "\n")

print("=== Generated Pattern 2 (Simulated Thumb Flow) ===")
fake_pattern_2 = generator_2.generate(length=180)
print(fake_pattern_2)