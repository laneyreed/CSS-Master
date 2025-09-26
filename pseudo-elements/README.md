# Pseudo Elements
**Learn how to create decorative elements without additional HTML markup. This project demonstrates:**
- Empty pseudo-element creation with `content: ""`
- Positioning techniques using `absolute` and `relative`
- Perfect centering with `transform: translateX(-50%)`
- Creating decorative lines and visual elements


## 🎨 CSS Concepts Covered

- ✅ Pseudo-elements (`::before`, `::after`)
- ✅ CSS Positioning (`absolute`, `relative`)
- ✅ CSS Transforms
- ✅ Centering techniques


### Empty Pseudo Element
- `pseudo-element.html ` and `styles.css`
```
.card-title {
    position: relative;
}
```
- `position: relative;`
    -  Critical! Allows the `::after` pseudo-element to position relative to the element with the `card-title` class

```
.card-title::after {
  content: "";
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
}
```
- `position: absolute;`: Positions the decorative line relative to the card title
- `bottom: -10px`: Places the line 10px below the bottom edge of the title text
- `left: 50%`: Positions the line's left edge at the horizontal center of the title
- `transform: translateX(-50%)`: Perfect centering technique:
    - Moves the line left by 50% of its own width
    - This centers the 60px line perfectly under the title, regardless of title length
- `width: 60px; height: 4px`: Creates a 60px wide, 4px tall decorative line

#### Why This Technique is Powerful
- No extra HTML needed - Pure CSS decoration
- Automatically centers regardless of title length