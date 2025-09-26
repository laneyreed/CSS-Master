# 🎨 Responsive Banner

## 🚀 Overview
**A standalone professional-grade, production-ready hero banner that draws attention without overwhelming. The compoenet can be used as a reusable, self-contained component and integrated into larger projects**


### ✨ Demonstrates

✅ Animations

✅ Gradients

✅ Responsive Design


### 🎯 Project Purpose

- Demonstrate use of Keyframe Animations
    - `backgroundShift` 
    - `fadeInUp`

#### 🎯 Keyframe Animation: `backgroundShift`
- this animation is used on the banner's background overlay and creates a diagonal floating motion
- total horizontal movement: 20px (from -10px to +10px)
- total vertical movement: 20px (from -10px to +10px)
- direction: moves from top-left to bottom-right and back
```
@keyframes backgroundShift {
0% { transform: translateX(-10px) translate(-10px); }
100% { transform: translateX(10px) translate(10px); }
}
```

- **`@keyframes backgroundShift`** - Defines a named animation sequence
    - **`0%`** Starting state of the animation
    - **`100%`** Ending state of the animation
- **`transform`**
    - Start Position (0%): `translateX(-10px) translateY(-10px)`
        - Moves the element 10px left and 10px up from its original position
    - End Position (100%): `translateX(10px) translateY(10px)`
        - Moves the element 10px right and 10px down from its original position

- Animation applied on the banner's background overlay
    ```
    .hero-banner::before {
    animation: backgroundShift 20s ease-in-out infinite alternate;
    }
    ```

    - **Duration: `20s`**: Very slow, subtle movement
    - **Timing: `ease-in-out`**: Smooth acceleration and deceleration
    - **Repeat: `infinite`**: Continuously loops
    - **Direction: `alternate`**: Reverses direction each cycle

#### ✨ Keyframe Animation: `fadeInUp`
- this animation creates a "slide up and fade in" entrance
- element starts invisible and 30px below its final position
- simultaneously fades in while sliding upward
- ends at full opacity in its natural position
```
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```
- **`@keyframes fadeInUp`** defines a named animation called "fadeInUp"
    - **`from`** starting state (equivalent to 0%)
        - **`opacity: 0`** element is completely invisible
        - **`transform: translateY(30px)`** element is positioned 30px below its final position
    - **`to`** ending state (equivalent to 100%)
        - **`opacity: 1`** Element becomes fully visible
        - **`transform: translateY(0)`** Element moves to its natural position

- Animation applied on banner headline ans subheadline
```
.banner-headline {
    animation: fadeInUp 1s ease-out;
}
```
- **Duration:** 1 second
- **Timing: `ease-out`** (fast start, slow finish)
- **Delay:** None - starts immediately

```
.banner-subheadline {
    animation: fadeInUp 1s ease-out 0.3s both;
}
```
- **Duration:** 1 second
- **Timing: `ease-out`**
- **Delay: `0.3s`** starts after headline begins
- **Fill Mode: `both`** maintains start and end states

- creates a staggered animation effect that is a choreographed entrance sequence
    - **`0.0s:`** Headline starts fading in and sliding up
    - **`0.3s:`** Subheadline starts its animation (while headline is mid-animation)
    - **`1.0s:`** Headline animation completes
    - **`1.3s:`** Subheadline animation completes


### Accessibility
```
@media (prefers-reduced-motion: reduce) {
    .banner-headline,
    .banner-subheadline {
        animation: none;
    }
}
```
- respects users who prefer reduced motion for accessibility reasons

- **`@media (prefers-contrast: high)`**: CSS media feature that detects when users have enabled high contrast mode
    - automatically triggers when system-level high contrast settings are active
    - works across Windows High Contrast, macOS Increase Contrast, and browser settings