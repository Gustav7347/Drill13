# Drill13 PRD

## Goal

Add an item-selection overlay to the LEC15 game framework project. The overlay lets the player choose the projectile behavior while playing.

## Requirements

1. Pressing `I` during play toggles item mode on; the `item_select.png` image is shown over the game.
2. Pressing `I` again closes item mode.
3. Number keys affect projectile selection only while item mode is open:
   - `0`: disable projectile firing.
   - `1`: use the 21x21 ball image (`ball21x21.png`).
   - `2`: use the 41x41 ball image (`ball41x41.png`).
4. Number keys pressed outside item mode do not change the current selection.
5. Preserve the existing logo, title, play, and pause flows.

## Implementation plan

1. Commit this PRD before implementation.
2. Add the LEC15 framework source and required assets to this standalone Drill13 repository.
3. Add the item-mode overlay and selection controls to the play flow.
4. Apply the selected projectile size, including the no-projectile option.

## Validation

- Compile the changed Python modules without launching the game.
- Check that item-mode input is isolated from normal play input and that projectile selection changes only through item-mode input.
