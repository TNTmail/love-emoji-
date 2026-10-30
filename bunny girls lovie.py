import tkinter as tk
import tkinter

class HeartAnimation:
    def __init__(self, root):
        self.root = root
        
        # Make the window borderless and maximize/fullscreen
        self.root.title("Love Animation")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        
        # Press Escape key to close the window easily
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Canvas that fills the maximized window
        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Pulsing parameters
        self.size = 100
        self.min_size = 80
        self.max_size = 350
        self.growth_rate = 6
        
        # Start the loop
        self.animate()

    def draw_heart(self, cx, cy, size):
        self.canvas.delete("heart")
        
        # Construct heart coordinates using cubic Bezier curves
        # Scaling curve points relative to center (cx, cy) and size
        points = [
            cx, cy - 0.2 * size,                     # Top center indent
            cx + 0.5 * size, cy - 0.8 * size,         # Left bump top
            cx + 1.0 * size, cy - 0.2 * size,         # Left side
            cx, cy + 0.8 * size,                     # Bottom tip
            cx - 1.0 * size, cy - 0.2 * size,         # Right side
            cx - 0.5 * size, cy - 0.8 * size,         # Right bump top
            cx, cy - 0.2 * size                      # Back to start
        ]
        
        # Draw smooth red heart shape
        self.canvas.create_polygon(
            points, 
            smooth=True, 
            fill="#FF2E63", 
            outline="#FF6B6B", 
            width=4, 
            tags="heart"
        )

    def animate(self):
        # Center coordinates based on window size
        cx = self.root.winfo_width() / 2
        cy = self.root.winfo_height() / 2

        # Draw frame if window geometry is ready
        if cx > 1 and cy > 1:
            self.draw_heart(cx, cy, self.size)

            # Pulsing logic
            self.size += self.growth_rate
            if self.size >= self.max_size or self.size <= self.min_size:
                self.growth_rate *= -1  # Reverse direction

        # Run next frame in 16 milliseconds (~60 FPS)
        self.root.after(16, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartAnimation(root)
    root.mainloop()