This is a structured layout of the current project.
## Objects
### `List`
The container where `ListItem`s are stored.<br/><br/>
Attributes:
- `_persistent` - boolean, does the list stay around when it is empty, or get archived/deleted?
- `display_name` - The user-defined name for display.
- `_items` - array of `ListItem`s that are on this list.
### `ListItem`
For use with single items.<br/><br/>
Attributes:
- `_completion_status` - Enum "Completed", "Incomplete", "Partially Complete", "In Progress", "On the backburner", "Abandoned". Should have designated setter method.
- `is_time_sensitive` - boolean, self-explanatory.
- `_recurrance` - Enum
- `recurrance_interval` - int, number of seconds in between occurrences of a recurring item. Default is -1 for non-recurring items.

### `Project`
- Multiply inherits from both `List` & `ListItem`, because it both stores other `ListItem`s & is itself a `ListItem` to be stored on a `List`.
## Views
### Temporal Views
- Day Overview
- Week Overview
- Month Overview
### Item Views
- `ListItem` Detail view
- Edit `ListItem`
- `Project` Overview
- Edit `Project` Contents