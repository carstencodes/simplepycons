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


class ArmKeilIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "armkeil"

    @property
    def original_file_name(self) -> "str":
        return "armkeil.svg"

    @property
    def title(self) -> "str":
        return "Arm Keil"

    @property
    def primary_color(self) -> "str":
        return "#394049"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Arm Keil</title>
     <path d="M3.028
 10.06h.9v3.863h-.9v-.404c-.288.339-.712.53-1.157.523-1.19
 0-1.871-.99-1.871-2.055 0-1.257.863-2.028 1.881-2.028.448-.01.874.195
 1.147.55v-.45zm-2.11 1.945c0 .67.422 1.23 1.073 1.23.567 0 1.092-.413
 1.092-1.221 0-.844-.523-1.248-1.092-1.248-.651 0-1.073.554-1.073
 1.239zm4.08-1.945h.9v.349c.107-.127.234-.235.376-.321.168-.093.358-.138.55-.13.248-.005.492.059.706.185l-.367.816a.812.812
 0 0 0-.459-.138c-.192
 0-.385.028-.56.211-.246.266-.246.633-.246.89v2h-.9V10.06zm3.113
 0h.9v.358a1.19 1.19 0 0 1 .954-.46c.411-.006.794.212 1
 .568.32-.457.807-.567 1.147-.567.468 0 .88.22
 1.102.606.073.128.202.412.202.972v2.386h-.9v-2.129c0-.431-.046-.606-.083-.688a.511.511
 0 0 0-.514-.34.664.664 0 0
 0-.532.283c-.156.221-.175.551-.175.882v1.992h-.899v-2.129c0-.431-.046-.606-.082-.688a.511.511
 0 0 0-.514-.34.664.664 0 0
 0-.532.283c-.157.221-.175.551-.175.882v1.992h-.9V10.06zm7.317 1.657
 1.645-1.656h.579l-1.807 1.8 1.865
 2.061h-.59l-1.581-1.772-.11.11v1.662H15V10.06h.429v1.657zm4.865-1.252h-1.575v1.147h1.531v.405h-1.531v1.5h1.575v.405h-2.004V10.06h2.004v.405zm1.216-.405v3.862h-.428V10.06h.428zm1.425
 0v3.46H24v.405h-1.494V10.06h.428z" />
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
