// ナビゲーションドロワーイベントハンドラ
class NavDrawer {
    constructor(toggleId, dummyId) {
        // ドロワー開閉状態管理要素
        this.checkbox = document.getElementById(toggleId);
        // ドロワー以外の領域判定用要素
        this.dummy = document.getElementById(dummyId);
        // 画面の向き情報
        const landscape = window.matchMedia("(orientation: landscape)");

        this.checkbox.addEventListener('change', () => this.toggleDummy());
        this.dummy.addEventListener('click', () => this.close());

        // 画面の向きが横に変更されたらドロワーを閉じる
        landscape.addEventListener("change", () => {
            this.close()
        });

        // 初期状態
        this.toggleDummy();
    }

    toggleDummy() {
        // ダミーの表示非表示切り替え
        this.dummy.style.display = this.checkbox.checked ? 'block' : 'none';
    }

    close() {
        // ドロワーを閉じる
        if (this.checkbox.checked) {
            this.checkbox.checked = false;
            this.checkbox.dispatchEvent(new Event('change'));
        }
    }
}

function setDarkMode(btn, enabled) {
    if (enabled) {
        document.body.classList.add('dark-mode');
        document.cookie = "darkmode=1;path=/;max-age=31536000";
    } else {
        document.body.classList.remove('dark-mode');
        document.cookie = "darkmode=0;path=/;max-age=31536000";
    }
    btn.innerHTML = enabled ? "☀️" : "🌙";
}

function getDarkModeFromCookie() {
    return document.cookie.split(';').some(c => c.trim() === "darkmode=1");
}

document.addEventListener('DOMContentLoaded', function () {
    // ボタンで切り替え
    const btn = document.getElementById('toggle-darkmode');

    // 初期状態
    setDarkMode(btn, getDarkModeFromCookie());

    if (btn) {
        btn.addEventListener('click', function () {
            setDarkMode(btn, !document.body.classList.contains('dark-mode'));
        });
    }
});

// 初期化
window.addEventListener('DOMContentLoaded', () => {
    new NavDrawer('nav-menu-toggle', 'dummy');
});