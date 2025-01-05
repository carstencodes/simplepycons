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


class CodecademyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codecademy"

    @property
    def original_file_name(self) -> "str":
        return "codecademy.svg"

    @property
    def title(self) -> "str":
        return "Codecademy"

    @property
    def primary_color(self) -> "str":
        return "#1F4056"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codecademy</title>
     <path d="M23.827 19.729h-5.595c-.094 0-.17.058-.17.172v1.515c0
 .094.058.17.172.17h5.594c.096 0
 .172-.044.172-.164v-1.515c0-.105-.057-.166-.173-.166v-.014zM16.463
 2.463c.016.034.03.067.047.12v18.79c0 .06-.02.096-.037.114a.168.168 0
 01-.135.06H.153c-.038 0-.075 0-.097-.02A.181.181 0 010
 21.393V2.564c0-.076.04-.134.096-.15h16.242c.04 0
 .096.017.115.034v.016zM1.818 19.573c0
 .072.038.135.096.152h12.643c.058-.019.096-.076.096-.154V4.402c0-.073-.039-.134-.098-.15H1.915c-.056.02-.096.073-.096.15l-.003
 15.17zm5.174-8.375c.65 0 1.014.177
 1.396.62.058.074.153.093.23.034l1.034-.92c.075-.044.058-.164.02-.224-.635-.764-1.554-1.244-2.74-1.244-1.59
 0-2.79.795-3.255 2.206-.165.495-.24 1.126-.24 1.98 0 .854.075
 1.483.255 1.98.465 1.425 1.665 2.204 3.255 2.204 1.2 0 2.115-.48
 2.745-1.216.045-.074.06-.165-.015-.226l-1.037-.915c-.073-.047-.163-.047-.224.027-.39.45-.795.69-1.454.69-.706
 0-1.245-.345-1.47-1.035-.136-.39-.166-.87-.166-1.483
 0-.615.045-1.068.18-1.47.24-.66.766-1.008 1.486-1.008z" />
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
