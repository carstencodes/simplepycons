#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class PlayerFmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playerfm"

    @property
    def original_file_name(self) -> "str":
        return "playerfm.svg"

    @property
    def title(self) -> "str":
        return "Player FM"

    @property
    def primary_color(self) -> "str":
        return "#C8122A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Player FM</title>
     <path d="M11.976 0a12 12 0
 00-.347.012c-.323.021-.771.063-1.129.11-3.29.448-6.096 2.1-7.993
 4.56a12.027 12.027 0 00-1.22 1.94 12 12 0
 00-.173.358c-.092.198-.179.4-.261.603a12 12 0
 00-.288.788l-.045.143A12 12 0 000 11.986v.037A12 12 0 0012 24a12 12 0
 0011.939-10.79l.003-.024A12 12 0 0024 12.018v-.048a12 12 0
 00-.769-4.182c-.04-.105-.081-.21-.125-.313a12 12 0
 00-.226-.507c-1.487-3.15-4.299-5.59-7.698-6.506-.76-.208-1.978-.39-2.813-.444A12
 12 0 0012.024 0h-.048zm2.321 2.88c.166.001.377.056.675.159 1.782.611
 3.773 2.157 4.856 3.764.752 1.118 1.337 2.428 1.337 2.987 0
 .358-.35.681-.725.681-.35
 0-.708-.305-.804-.68-.13-.525-.83-1.852-1.345-2.534-.917-1.205-2.332-2.262-3.72-2.777-.979-.367-1.232-.795-.778-1.336.152-.182.29-.267.504-.265zm-3.885
 1.4c.26.001.495.056.7.165 1.31.664 1.24 2.568-.122
 3.092-1.686.637-2.533 1.319-3.084 2.437-1.153 2.34-.21 5.1 2.123
 6.218 1.712.821 3.668.533 5.03-.725.62-.576.961-1.074
 1.267-1.878.428-1.126.917-1.545 1.79-1.545 1.119 0 1.887.943 1.66
 2.026-.463 2.13-2.253 4.27-4.42
 5.275-1.196.55-1.851.69-3.362.69-1.485
 0-2.131-.131-3.284-.655-3.144-1.424-5.075-4.83-4.673-8.21a8.123 8.123
 0
 015.511-6.734c.315-.105.603-.157.864-.156zm3.463.96c.217.004.499.105.914.306
 1.686.803 3.083 2.279 3.834 4.035.28.672.14 1.109-.41
 1.283-.42.123-.7-.104-1.066-.864-.681-1.441-1.65-2.437-3.013-3.11-.795-.384-.891-.471-.97-.847-.035-.2
 0-.314.184-.532.157-.184.31-.276.527-.271zm-.398
 2.443c.23-.001.496.108.84.334.961.629 2.044 1.983 2.044 2.55 0
 .289-.28.656-.559.725-.376.097-.646-.087-1.04-.707-.427-.655-.925-1.153-1.44-1.415-.446-.227-.577-.402-.577-.769a.58.58
 0 01.245-.515.727.727 0 01.487-.203z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
