<!DOCTYPE html>
<html>
<head>
    <title>De Castro ACT 1</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f9f9f9;
        }
        .container {
            background: white;
            padding: 110px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            font-weight: bold;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input[type="text"], input[type="email"], input[type="date"] {
            width: 100%;
            padding: 5px;
            margin-top: 5px;
        }
        .gender {
            margin-top: 10px;
        }
        .gender input {
            margin-right: 5px;
        }
        input[type="submit"] {
            margin-top: 15px;
            padding: 8px 16px;
        }
        .success {
            color: green;
            font-weight: bold;
            margin-top: 20px;
        }
        .output {
            margin-top: 10px;
        }
        input[type="submit"] {
            font-weight: bold; 
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Sign Up Form</h2>

    <form class="profile" method="post">
        <label>Name:</label>
        <input type="text" name="name" required>

        <label>Address:</label>
        <input type="text" name="address" required>

        <label>Email:</label>
        <input type="email" name="email" required>

        <label>Phone Number:</label>
        <input type="text" name="phone" required>

        <label class="gender">Gender:</label>
        <input type="radio" name="gender" value="Male" required> Male
        <input type="radio" name="gender" value="Female"> Female
        <input type="radio" name="gender" value="Other"> Other

        <label>Date of Birth:</label>
        <input type="date" name="dob" required>

        <input type="submit" name="submit" value="Sign Up">
    </form>

    <?php
    if (isset($_POST['submit'])) {
        echo "<p class='success'>Sign-Up Successful!</p>";
        echo "<div class='output'>";
        echo "<strong>Name:</strong> " . htmlspecialchars($_POST['name']) . "<br>";
        echo "<strong>Address:</strong> " . htmlspecialchars($_POST['address']) . "<br>";
        echo "<strong>Email:</strong> " . htmlspecialchars($_POST['email']) . "<br>";
        echo "<strong>Phone:</strong> " . htmlspecialchars($_POST['phone']) . "<br>";
        echo "<strong>Gender:</strong> " . htmlspecialchars($_POST['gender']) . "<br>";
        echo "<strong>Date of Birth:</strong> " . htmlspecialchars($_POST['dob']) . "<br>";
        echo "</div>";
    }
    ?>
</div>

</body>
</html>
