import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Window 2.2
import myapp 1.0

ApplicationWindow {
  visible: true
  width: 640
  height: 480
  title: qsTr("My App")

  MyComponent {
    id: myComp

    Component.onCompleted: {
      // myComp.someValueChanged.connect(callback) // [3] fails
      myComp["some_value_changed"].connect(callback) // [3]

      console.log("myComp some_value: snake_case access: " + myComp["some_value"] + " camelCase access: " + myComp.someValue) // [1]
      // myComp.someValue = 20 // [1] fails
      myComp["some_value"] = 20 // [1]

      // myComp.someSlot(25) // [2] fails
      myComp["some_slot"](25) // [2]
    }

    // onSomeValueChanged: callback(someValue) [3]

    function callback(value) {
      console.log("some_value changed " + value)
    }
  }
}
