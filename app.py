<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<!-- Thêm font Robot từ Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <!-- Thêm Font Awesome cho các icon ngân hàng -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <title>Shop Huấn Hà🌎</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="https://cdn.vinaenter.edu.vn/wp-content/uploads/2024/08/hinh-nen-wibu.jpg" type="image/png">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
</head>
<body>   
    <div id="particles-js"></div>   
<!-- Thêm thẻ audio để phát nhạc tự động -->
    <audio id="background-music" autoplay loop>
        <source src="https://files.catbox.moe/wody9q.mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
<!-- Form Thông Báo khi vào trang web -->
<div id="welcome-form" class="welcome-form">
    <div class="form-content">
        
       <li>
  <i class="fas fa-comments">Hà Văn Huấn !
Dịch Vụ Hỗ Trợ Game Hack Game , Data Hack Game Antiband , Files Hỗ Trợ Kéo Tâm Uy Tín Chất Lượng Cao</i>
<i class="fas fa-coins"></i> • Mọi Thắc Mắc Liên Hệ Qua Zalo 0325575642
</li>
      
<button class="close-menu-btn" onclick="closeWelcomeForm()">Đóng</button>
        
</h2>
    </div>
</div>

    <!-- Menu Chứa các mục -->
    <div id="menu" class="hidden">
        <ul>
            <li><i class="fas fa-coins" onclick="openDepositOptions()"></i> Nạp Tiền<!-- Coins Icon --></li>
        </ul>
<ul>
    <li>
<i class="fas fa-envelope" onclick="location.href='contact_form.html'"></i>Liên Hệ
        
    </li>
</ul>
<ul>
    <li>
<i class="fas fa-comment-alt" onclick="location.href='chatbot.html'"></i> ChatBot 
        
    </li>
</ul>
<ul>
    <li>
<i class="fas fa-clock" onclick="location.href='thanhtoannhanh.html'"></i> Nạp Nhanh
        
    </li>
</ul>
<ul>
    <li>
<i class="fas fa-user-shield" onclick="location.href='admin_login.html'"></i> Admin
        
    </li>
</ul>
<ul>
<li>
 <i class="fas fa-home" onclick="toggleMenu()"></i> Trang Chủ      
</ul>
</li>
<ul>
<li>
<a href="profiles.html"><i class="fas fa-info" href="profiles.html"></i>Thông Tin</a>
</ul>
</li>
    </div>

    <!-- Mục Nạp Tiền -->
    <div id="deposit-options" class="hidden">
        <button onclick="openBankDeposit()">Nạp Bank</button>
        <button onclick="openCardDeposit()">Nạp Thẻ Cào</button>
          <button class="close-menu-btn" onclick="closeDepositOptions()">Đóng</button>
    </div>

    <!-- Form Nạp Bank -->
    <div id="bank-deposit" class="hidden">
            <h3><strong>Thông tin tài khoản Ngân Hàng:</strong></h3>
    <p><strong>
Ngân Hàng:</strong> Mb Bank</p>
        <p><strong>Số tài khoản:</strong> 0325575642 <button class="copy-btn" onclick="copyToClipboard('1234567890')"><img src="https://i.imgur.com/iaGxoPH.png" alt="Sao chép"></button></p>
    <p><strong>Chủ Tài Khoản:</strong> Hà Văn Huấn </p>
       <p><strong>Mã Nạp:</strong> <span id="deposit-code"></span> <button class="copy-btn" onclick="copyToClipboard(document.getElementById('deposit-code').innerText)"><img src="https://i.imgur.com/iaGxoPH.png" alt="Sao chép"></button></p> 
        <button class="close-menu-btn" onclick="closeBankDeposit()">Đóng</button>
    </div>

    <!-- Form Nạp Thẻ Cào -->
    <div id="card-deposit" class="hidden">
        <h3>Nhập thông tin thẻ cào:</h3>
        <input type="text" id="seri" placeholder="Nhập seri thẻ cào" required>
        <input type="text" id="pin" placeholder="Nhập mã thẻ cào" required>
                <button onclick="submitCard()">Gửi</button>
        <button class="close-menu-btn" onclick="closeCardDeposit()">Đóng</button>
    </div>

    <!-- Đóng menu -->
    <div id="overlay" class="overlay hidden" onclick="toggleMenu()"></div>
 <!-- Kết Nối Đi nào menu 3 gạch -->
<div id="auth">
            <button id="register-btn">Đăng Ký</button>
            <button id="login-btn">Đăng Nhập</button>
        </div>
        
    <main>
        <div id="form-container">
            <!-- Form đăng ký -->
            <form id="register-form" class="hidden">
            <span class="close-btn" onclick="closeForm('register-form')">X</span>
                <h2>Đăng Ký</h2>
                <label for="register-username">Tên người dùng:</label>
                <input type="text" id="register-username" placeholder="Nhập tên người dùng" required>
                <label for="register-password">Mật khẩu:</label>
                <input type="password" id="register-password" placeholder="Nhập mật khẩu" required>
                        <button type="button" onclick="register()">Đăng Ký</button>
            </form>
            
            <!-- Form đăng nhập -->
            <form id="login-form" class="hidden">
        <span class="close-btn" onclick="closeForm('login-form')">X</span>
                <h2>Đăng Nhập</h2>
                <label for="login-username">Tên người dùng:</label>
                <input type="text" id="login-username" placeholder="Nhập tên người dùng" required>
                <label for="login-password">Mật khẩu:</label>
                <input type="password" id="login-password" placeholder="Nhập mật khẩu" required>
                <button type="button" onclick="login()">Đăng Nhập</button>
            </form>
        </div>
        
        
    </main>
    <header>
    <section class="product">
<!-- Khu vực hiển thị profile sau khi đăng nhập -->
<!-- Menu 3 gạch ở góc phải -->
    <div id="menu-toggle" class="menu-container" onclick="toggleMenu()">
      <span></span>
      <span></span>
      <span></span>
    </div>
        <div id="profile" class="hidden"> 
             <img src="https://i.pinimg.com/736x/aa/a6/fe/aaa6fe6e8ebebaf5fd5579ff717460ed.jpg" alt="User Icon" class="user-icon">
                <div id="username-display" class="blink-text"></i></div>
        </div>
             <button id="logout-btn" onclick="logout()">Đăng Xuất</button>
    </header>
    <main>
    </section>
<section class="product">
        <p> IP : <span id="ip-address">Đang tải...</span></p>
          <div class="stats">
            <i class="fas fa-eye"></i>
            <span id="visitor-count">Đang tải số lượng...</span>
<img src="https://i.imgur.com/pNU6xIm.png" alt="Hình ảnh 1">
  Lì xì đi nào ae ơi -))     
</div>    
</section>
<section class="product">
          <p class="small-font" style="color: #ff5722;">Thông Báo Ngày 29/1/2025 👀</p>
<i class="fas fa-user">Hà Văn Huấn</i>
<p>
• Nếu Có Bất Cứ Thắc Mắc Gì Hãy Liên Hệ Cho Admin <label>
  <a href="https://www.facebook.com/profile.php?id=61561543393412" target="_blank" style="text-decoration: none; color: blue;">
    Nhấn vào đây
  </a>
<i class="fas fa-heart"></i> <!-- Hiển thị icon hình trái tim --> <!-- Facebook Icon -->
<p><i class="fas fa-coins"></i>  <!-- Dollar Sign Icon --> • Chúng Tôi Vẫn Đang Hoạt Động Xuyên Ngày Đêm Để Suport Tất Cả Các Bạn , Hãy Mua Một Bản Và Ở Nhà Chơi Fai Fai Nào ! </p>
        <!-- Biểu tượng cảnh báo Bell -->
        <i class="fas fa-bell" style="color: orange;"></i>
        <span>Thông báo mới!</span>
<div id="marquee" class="multi-color">
        <span class="blinking-text">Các Khách Hàng Lưu Ý : Nếu Đã Chuyển Khoản Thì Hãy Liên Hệ Qua Số Zalo : 0325575642 Hoặc Liên Hệ Qua Faceboock Admin Để Được Suport Nhanh Chóng </span>
    </div>
</label>
</p>
</p>
    
  </section>
    <section class="product">
        <img src="https://viresa.org.vn/service-apis/uploads/large_luat_thi_dau_Freefire_b24c1bcbf7.jpg" alt="Hình ảnh 1">
        <h3>Hỗ Trợ Kéo Tâm Sử Dụng All Thiết Bị (Android , Ios )</h3>
        <p><strong>Giá: 50,000 VNĐ</strong></p>
        <button onclick="window.location.href='payment1.html'">Mua Ngay        <i class="fas fa-download"></i><span class="hot">HOT</span></button>
    </section>

    <section class="product">
        <img src="https://viresa.org.vn/service-apis/uploads/large_luat_thi_dau_Freefire_b24c1bcbf7.jpg" alt="Hình ảnh 2">
        <h3>Kéo Nhẹ Aim Đầu Bảo Hành Antiband , Sử Dụng Leo Rank All Map , Tử Chiến , Sinh Tồn (sử dụng 1Ob )</h3>
         <span class="original-price">150.000₫</span>
        <span class="discounted-price">80.000₫</span>
        <button onclick="window.location.href='payment2.html'">Mua Ngay        <i class="fas fa-tags sale-icon"></i><span class="hot">Sale</span></button>
    </section>

    <section class="product">
        <img src="https://viresa.org.vn/service-apis/uploads/large_luat_thi_dau_Freefire_b24c1bcbf7.jpg" alt="Hình ảnh 3">
        <h3>Sử Dụng Tất Cả Thiết Bị , Chỉ Càn Nhích Nhẹ Nút Bắn Là Hesot - Ghim đầu chặt Khi kéo ( Bảo Hành An toàn All Map)</h3>
        <span class="original-price">300.000₫</span>
        <span class="discounted-price">180.000₫</span>
<!-- Dropdown (Chọn Mục) -->
        <button onclick="window.location.href='payment3.html'">Mua Ngay      <i class="fas fa-tags sale-icon"></i><span class="hot">Sale</span></button>
    </section>

      <section class="product">
    <img src="https://viresa.org.vn/service-apis/uploads/large_luat_thi_dau_Freefire_b24c1bcbf7.jpg" alt="Hình ảnh 4">
    <h3>Bảo Hành All Khi Chơi - Leo Rank All Map Và Sử Dụng Tất Cả Ob</h3>
    <span class="original-price">500.000₫</span>
        <span class="discounted-price">280.000₫</span>

        <button onclick="window.location.href='payment4.html'">Mua Ngay        
        <i class="fas fa-tags sale-icon"></i><span class="hot">Sale</span></button>
  </section>

  <h1 class="blur-text">Hack Miễn Phí </h1>
 <section class="product">
    <img src="https://i.imgur.com/BTMaBlG.png" alt="Hình ảnh 4">
    <h3>Chơi Vô Tư - Chơi All Map</h3>
    <p><strong>Giá: 0.00 VNĐ</p></strong>
  <button onclick="window.location.href='https://link4m.com/hkgacI';"> <i class="fas fa-download">Tải Xuống</i></button>
</section>
<section>
   <!-- Phần menu liên hệ -->
  <div class="contact-menu">
    <h3>Liên hệ</h3>
    <!-- Icon Email -->
      <div><i class="fas fa-envelope"></i><span>Email: vanhuanha56@gmail.com</span></div>
      
      <!-- Icon Điện Thoại -->
      <div><i class="fas fa-phone-alt"></i><span>SĐT: +84 325 575 642</span></div>
<i class="fab fa-youtube"><a href="https://youtube.com/@huanbot-m7g?si=S_KG0nDRZNOuxQLI" target="_blank" style="text-decoration: none; color: blue;">
    Yutube
  </a></i>
</section>
</main>
<!-- Icon Telegram -->
        <a href="https://t.me/suporthuanha" target="_blank">
            <i class="fab fa-telegram" style="font-size: 40px; color: #0088cc;"></i>
        </a>
Telegram
        
        <!-- Icon Facebook -->
        <a href="https://www.facebook.com/profile.php?id=61561543393412" target="_blank">
            <i class="fab fa-facebook" style="font-size: 40px; color: #1877f2;"></i>
        </a>
Faceboock
        
        <!-- Icon Zalo -->
        <a href="https://zaloapp.com/qr/p/1s3nnmtozvd1l?src=qr" target="_blank">
            <i class="fab fa-facebook-messenger" style="font-size: 40px; color: #4c8bf5;"></i>
        </a>
Zalo
 <script src="script.js"></script>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            particles: {
                number: {
                    value: 100, // Số lượng hoa đào rơi
                    density: {
                        enable: true,
                        value_area: 500
                    }
                },
                color: {
                    value: "#ff69b4" // Màu sắc của hoa đào (hồng)
                },
                shape: {
                    type: "star", // Hình dạng của hạt là hình tròn
                    stroke: {
                        width: 0,
                        color: "#ffffff"
                    },
                    polygon: {
                        nb_sides: 5
                    }
                },
                opacity: {
                    value: 0.5,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 1,
                        opacity_min: 0
                    }
                },
                size: {
                    value: 5,
                    random: true,
                    anim: {
                        enable: true,
                        speed: 2,
                        size_min: 0.1
                    }
                },
                line_linked: {
                    enable: false // Tắt kết nối giữa các hạt
                },
                move: {
                    enable: true,
                    speed: 1,
                    direction: "bottom", // Di chuyển xuống dưới giống như hoa đào rơi
                    random: true,
                    straight: false,
                    out_mode: "out"
                }
            },
            interactivity: {
                events: {
                    onhover: {
                        enable: true,
                        mode: "repulse"
                    },
                    onclick: {
                        enable: true,
                        mode: "push"
                    }
                },
                modes: {
                    repulse: {
                        distance: 200,
                        duration: 0.4
                    },
                    push: {
                        particles_nb: 4
                    }
                }
            },
            retina_detect: true
        });
    </script>

    <script>
        // Sử dụng API ipify để lấy IP
        fetch('https://api.ipify.org?format=json')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ip-address').innerText = data.ip;
            })
            .catch(error => {
                console.log('Không thể lấy IP', error);
                document.getElementById('ip-address').innerText = 'Không thể lấy IP';
            });

        // Giả sử bạn lưu trữ số lượng người truy cập trên server hoặc trong LocalStorage
        // Cách đơn giản là sử dụng LocalStorage để lưu trữ số lượng người truy cập
        let visitorCount = localStorage.getItem('visitorCount');
        if (!visitorCount) {
            visitorCount = 1;  // Nếu chưa có, bắt đầu từ 1
        } else {
            visitorCount = parseInt(visitorCount) + 1;
        }

        localStorage.setItem('visitorCount', visitorCount);
        document.getElementById('visitor-count').innerText = visitorCount;
 </script>
</body>
</html>

Thêm Coder form thanh toán ngân hàng online và số tiền thanh toán , có nút xác nhận thanh toán , và cổng thanh toán sẽ hoạt động bằng token ip ngân hàng , khi người dùng chuyển thành công thì Token ip sẽ hoạt động và hiển thị thành công
