if [ "$1" == "" ]; then
  echo "You must specify a message"
  exit 1
fi

git commit -am"$1" || exit 1
git push
