class NavDrawer {
    constructor(toggleId, dummyId) {
        this.checkbox = document.getElementById(toggleId);
        this.dummy = document.getElementById(dummyId);

        this.checkbox.addEventListener('change', () => this.toggleDummy());
        this.dummy.addEventListener('click', () => this.close());

        // 初期状態
        this.toggleDummy();
    }

    toggleDummy() {
        this.dummy.style.display = this.checkbox.checked ? 'block' : 'none';
    }

    close() {
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