<!DOCTYPE html>
<html lang="ka">
<head>
    
    <title</title>
    <style>
        #shape {
            width: 100px;
            height: 100px;
            background-color: blue;
            position: relative;
            transition: all 0.3s;
        }
    </style>
</head>
<body>
    <div id="shape"></div>

    <script>
        const shape = document.getElementById('shape');

        shape.addEventListener('mouseenter', () => {
            shape.style.borderRadius = '50%';
            shape.style.transform = 'translateX(50px)';
        });

        shape.addEventListener('mouseleave', () => {
            shape.style.borderRadius = '0';
            shape.style.transform = 'translateX(0)';
        });
    </script>
</body>
</html>