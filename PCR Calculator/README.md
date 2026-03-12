# 📊 PCR (Put Call Ratio) Calculator

A simple tool to calculate the **Put Call Ratio (PCR)** from options data.
PCR is a widely used indicator in the **stock market and options trading** to understand market sentiment.

This tool helps traders quickly compute the PCR value using **Put Open Interest and Call Open Interest**.

---

## 📌 What is Put Call Ratio (PCR)?

The **Put Call Ratio** is a sentiment indicator that measures the ratio of **Put options to Call options**.

It is commonly used to analyze whether the market is **bullish or bearish**.

### Formula

```
PCR = Total Put Open Interest / Total Call Open Interest
```

---

## 📈 Interpretation of PCR

| PCR Value     | Market Sentiment         |
| ------------- | ------------------------ |
| PCR < 1       | Bullish sentiment        |
| PCR = 1       | Neutral market           |
| PCR > 1       | Bearish sentiment        |
| Very High PCR | Possible market reversal |

---

## 🛠 Features

* Calculate **Put Call Ratio instantly**
* Works with **Options Open Interest data**
* Simple and lightweight tool
* Useful for **NIFTY / BANKNIFTY / Stock options analysis**

---

## 📂 Project Structure

```
pcr_calculator/
│
├── pcr_calculator.py
├── example_data.csv
└── README.md
```

---

## ⚙ How It Works

1. Collect **Put Open Interest**
2. Collect **Call Open Interest**
3. Apply the PCR formula

Example:

```
Put OI = 120000
Call OI = 100000

PCR = 120000 / 100000
PCR = 1.2
```

This indicates **bearish sentiment** in the market.

---

## 🚀 Future Improvements

Planned features for future versions:

* Automatic **option chain data fetching**
* **Visualization of PCR trends**
* **Strike-wise PCR calculation**
* **Integration with stock market APIs**

---

## 📊 Use Cases

This tool can be used for:

* Options trading analysis
* Market sentiment analysis
* Trading strategy development
* Algorithmic trading research

---

## ⚠ Disclaimer

This project is for **educational and research purposes only**.

It should **not be considered financial advice**.
Always perform your own analysis before making trading decisions.

---

⭐ If you find this project useful, consider **starring the repository**.
