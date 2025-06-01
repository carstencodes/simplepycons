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


class MyobIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "myob"

    @property
    def original_file_name(self) -> "str":
        return "myob.svg"

    @property
    def title(self) -> "str":
        return "MYOB"

    @property
    def primary_color(self) -> "str":
        return "#7B14EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MYOB</title>
     <path d="m11.276 9.347-1.254 3.346a366.37 366.37 0 0
 1-1.325-3.346H7.275l2.038 5.132-.86 2.063h1.38l2.845-7.195ZM5.083
 10.46c.551 0 .818.33.818
 1.01v3.112h1.314v-3.259c0-1.241-.853-2.108-2.075-2.108-.588
 0-1.127.206-1.516.58l-.016.015-.016-.015c-.39-.374-.926-.58-1.512-.58-1.225
 0-2.08.867-2.08 2.108v3.26h1.314V11.47c0-.68.267-1.01.818-1.01.552 0
 .819.33.819
 1.01v3.112h1.314V11.47c0-.68.267-1.01.819-1.01zm18.2-.398c-.494-.547-1.191-.849-1.962-.849a2.56
 2.56 0 0 0-1.521.497V7.458h-1.315v4.51c0 .721.258 1.396.725
 1.9.512.553 1.215.846 2.035.846.819 0 1.52-.293
 2.03-.845.467-.505.725-1.18.725-1.9a2.83 2.83 0 0
 0-.717-1.908Zm-2.039 3.405c-.937 0-1.446-.772-1.446-1.499
 0-.726.51-1.509 1.446-1.509.937 0 1.442.778 1.442 1.51 0 .73-.505
 1.498-1.442 1.498m-5.965 1.248c1.788 0 2.753-1.418 2.753-2.753
 0-1.334-.965-2.752-2.753-2.752-1.789 0-2.753 1.418-2.753 2.753 0
 1.335.964 2.753 2.753 2.753zm.001-1.248c-.936 0-1.445-.773-1.445-1.5
 0-.728.509-1.511 1.445-1.511s1.441.778 1.441 1.51c0 .733-.505
 1.501-1.441 1.501" />
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
