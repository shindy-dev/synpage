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

// 初期化
window.addEventListener('DOMContentLoaded', () => {
    new NavDrawer('nav-menu-toggle', 'dummy');
});