function Addtask(){
  let newtasks = document.getElementById('newtasks').value;
  let lists = document.getElementById('lists');
  let rows = document.createElement('div');
  let checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.className = 'checkbox';
  let box = document.createElement('div');
  let span = document.createElement('span');
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
    rows.appendChild(box);
    rows.appendChild(addclick);
    lists.append(rows);
    document.getElementById('newtasks').value = '';
  }

  addclick.onclick = function (){
    lists.removeChild(rows);
  }
}
