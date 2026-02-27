
## **Project Overview**

This repository contains the findings of a unique AI benchmark conducted on February 27, 2026\.

Instead of testing logic puzzles or coding abilities, this project evaluates the **"Physical World Perception" (Embodied AI intuition)** of mainstream Large Language Models (Fast/Instant Tier). By analyzing a sequence of seemingly meaningless "gibberish" typed by a human, the test reveals which AIs simply count letters, which ones get stuck on wrong assumptions, and which ones can successfully reverse-engineer the user's physical device, hand posture, and even muscle memory derived from rhythm games.

## **The Test Cases (Raw Prompts)**

The benchmark consists of two rounds of inputs, executed on a smartphone virtual keyboard.

**Round 1: The "Alternating Tapping" Phase**

**Prompt:** 这是我随机输入的一串字母，总结其中的规律： vdjbdhdhdhgdhdgdhnehdbdhenxhbdgfkwgduwkudhbwbjxghwkxgebxbuebxhnwvxywbhxyhwgxgwhxhjebxywnxhenxfunwkckwnvckwixhskcjhannxuwnvyxksgcuwkbxhwnxgejzkgbfhuwkgdhdjanvdgivehdhejbdbsjhfhdnkebehzhbrgxysjxjskwnhxhr

**Round 2: The "Thumb Fan-Sweep" Phase**

**Prompt:** 对比上一串，分析这一串： bxhebxgbsgxjwgxhwhxghedhhebxhnshdhchhehchsnchejhdhdhejsbchejbxhejzhrhwujxhwjbzjwmchwljchwkxnejakwjhxjwjfhqkhxjqkdruksbchwjhdbdkajhfjwhchnwhxjebchjehzhejxyejwbchjwhchwjxhejkqkncnwoqcukwokcjwojxjsoebbcbrjdcbbdr dhjebdhenx

## **The Ground Truth**

To understand the AI's performance, here is the actual physical context behind the "gibberish":

1. **Device:** A smartphone virtual keyboard (compact spacing), not a PC physical keyboard.  
2. **Posture Evolution:**  
   * *Round 1:* Typed using alternating index and middle fingers (high-speed jumps, bottom-row focus).  
   * *Round 2:* Typed using two thumbs while holding the phone (movement restricted to the thumb's fan-shaped joint radius).  
3. **Behavioral Profiling:** The tester is a hardcore rhythm game player (**Muse Dash**, **Phigros**). The rapid, alternating keystrokes in Round 1 are a direct reflection of "Alternating Tapping" muscle memory.

## **🏆 Model Reasoning Tiers**

Based on the responses from various Fast-tier models, we categorized their cognitive depth into three tiers:

### **🥉 Tier 1: The Literal Statistician (Surface Level)**

* **Representatives:** Doubao Fast, GLM-5 Fast  
* **Behavior:** Failed to see beyond the token level. They either refused to analyze the "gibberish" or merely counted the frequency of characters (e.g., "h appears 15 times"). Zero spatial awareness.

### **🥈 Tier 2: The Rigid Mapper (PC Keyboard Fundamentalists)**

* **Representatives:** Claude Sonnet 4.6, Deepseek Instant, Qwen3.5-Plus  
* **Behavior:** Successfully mapped the letters to a QWERTY layout and identified spatial proximity (e.g., typing x-h or w-k). However, they suffered from a fatal blind spot: assuming a **physical PC keyboard**. This caused them to misjudge the feasibility of fast, long-span jumps, failing to explain the rapid alternations in Round 1\.

### **🥇 Tier 3: The Behavioral Profiler (High-Dimensional)**

* **Representatives:** Gemini 3.0 Fast  
* **Behavior:** Successfully executed spatial reverse-engineering. It deduced the smartphone grip posture (the fan-shaped clustering in Round 2\) and astonishingly correlated the high-frequency alternating clicking rhythm in Round 1 with the muscle memory of interactive rhythm games.
