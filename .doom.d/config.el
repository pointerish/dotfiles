;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-
(setq user-full-name "Josias Alvarado"
      user-mail-address "josiasjag@gmail.com")

(setq confirm-kill-emacs nil)

(setq doom-font (font-spec :family "Iosevka Term" :size 22 :weight 'normal)
      doom-big-font (font-spec :family "Iosevka Term" :size 30 :weight 'normal)
      doom-variable-pitch-font (font-spec :family "Iosevka Curly Slab" :size 22))

(after! vterm
  (set-popup-rule! "*doom:vterm-popup:" :size 0.40 :vslot -4 :select t :quit nil :ttl 0 :side 'right)
  (set-window-margins (selected-window) 2 2)
)

(when (display-graphic-p)
  (require 'all-the-icons))
(setq treemacs-display-current-project-exclusively t)
;; UI Doom Emacs Stuff
(setq doom-theme 'modus-vivendi
      doom-modeline-vcs-max-length 35
      doom-modeline-major-mode-icon t
      lsp-lens-enable nil
      lsp-ui-sideline-enable nil
      display-line-numbers-type 'relative)

(setq org-directory "~/org/")

(after! org
  (setq org-roam-directory "~/Documents/org/roam")
  (setq org-roam-index-file "~/Documents/org/roam/index.org"))

;; I don't like having that many menu sections on my Doom Dashboard, so I remove them all ;)
(setq +doom-dashboard-menu-sections nil)
;; The following is to set the fancy Doom dashboard image to either Happy octopus or Sad octopus depending on a roll dice:
(setq random-number (+ (random 6) 1))
(if (not (= (mod random-number 2) 0))
    (setq fancy-splash-image "~/Pictures/emacs/sad.png")
  (setq fancy-splash-image "~/Pictures/emacs/happy.png"))

;; Check whether tiling mode is active on PopOS and start Emacs maximized if not.
(if (string= (shell-command-to-string "gsettings get org.gnome.mutter edge-tiling") "true\n")
    (add-hook 'window-setup-hook 'toggle-frame-maximized t))

(use-package! nyan-mode
  :custom
  (setq nyan-cat-face-number 4)
  (setq nyan-animate-nyancat t) (setq nyan-wavy-trail t)
  :hook
  (doom-modeline-mode . nyan-mode))

(setq +doom-dashboard-functions
  '(doom-dashboard-widget-banner
    doom-dashboard-widget-shortmenu))
