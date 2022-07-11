function Addtask(){
  let newtasks = document.getElementById('newtasks').value.toUpperCase();
  let lists = document.getElementsByClassName('lists')[0];
  let rows = document.createElement('div');
  let checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.className = 'checkbox';
  let box = document.createElement('div');
  box.className = 'box';
  let span = document.createElement('div');
  span.className = 'line';


  let addclick;
  if (newtasks != '') {
    rows.className = 'row';
    addclick = document.createElement('img');
    addclick.src = 'images.png';
    addclick.className ='photo';
    span.append(newtasks);
    box.appendChild(checkbox);
    box.appendChild(span);
    box.appendChild(addclick)
    rows.appendChild(box);
    lists.append(rows);
    document.getElementById('newtasks').value = '';
  }

  addclick.onclick = function (){
    lists.removeChild(rows);
  }
}
