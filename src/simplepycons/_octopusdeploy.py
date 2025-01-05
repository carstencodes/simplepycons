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


class OctopusDeployIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "octopusdeploy"

    @property
    def original_file_name(self) -> "str":
        return "octopusdeploy.svg"

    @property
    def title(self) -> "str":
        return "Octopus Deploy"

    @property
    def primary_color(self) -> "str":
        return "#2F93E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Octopus Deploy</title>
     <path d="M2.18 18.212c1.805-1.162 3.928-3.162
 3.122-5.51-.437-1.282-1.046-2.379-1.127-3.762a8.478 8.478 0 0 1
 .515-3.46C6.31 1.14 11.126-.917 15.481.389c4.03 1.216 6.808 5.893
 5.119 9.973-.965 2.356-1.395 4.173.755 6.006.582.496 2 1.24 1.992
 2.123 0 1.163-2.27-.244-2.522-.445.286.503 3.138 3.487 1.325
 3.688-1.67.194-3.147-2.139-4.15-3.142-1.686-1.682-1.395 2.042-1.403
 2.81 0 1.212-.868 3.676-2.41
 2.072-1.27-1.321-.775-3.433-1.674-4.905-.968-1.612-2.58 1.612-2.983
 2.2-.45.66-2.713 3.844-3.596 2.147-.725-1.38.434-3.538
 1.007-4.785-.209.453-1.685 1.123-2.115 1.34a5.738 5.738 0 0
 1-3.057.706c-2.267-.163-.527-1.368.387-1.96l.023-.005z" />
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
