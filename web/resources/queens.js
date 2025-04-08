let isDragging = false;
document.addEventListener("mousedown", () => isDragging = true);
document.addEventListener("mouseup", () => isDragging = false);

document.querySelectorAll("td").forEach(cell => {{
    cell.addEventListener("mousedown", () => {{
        cell.style.backgroundColor = "blue";
    }});
    cell.addEventListener("mouseover", (event) => {{
        if (isDragging) event.target.style.backgroundColor = "blue";
    }});
}});