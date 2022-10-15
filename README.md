# Violet

Meet the world's first talking AI theraputic friend, built on OpenAI Whisper.


# Emotions.py

For our Emotions.py, we planned to use the mathetical equation to quantify happiness (Source can be found below):
H(t)=w_0+w_1 * ∑^t_j=1 (γ^{t−j}CR_j+w_2) + ∑^t_j=1 (γ^{t−j}EV_j+w_3) + ∑^t_j=1 (γ^{t−j}RPE_j

However, generations were considerably unpredictable. Even when turning down Temperature and Top P, we would be faced with undesirable results that simply regenerated the equation. Unforunately, since the happiness equation did not produce great results, we were forced to scrap its usage. This is likely due to the fact that OpenAI may not be trained to handle such a niche equation that sees rare usage, and such equation may have inaccuracies itself.

Sources:
Equation of Happiness - https://www.pnas.org/doi/full/10.1073/pnas.1407535111