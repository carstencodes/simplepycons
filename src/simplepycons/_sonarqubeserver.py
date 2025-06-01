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


class SonarqubeServerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonarqubeserver"

    @property
    def original_file_name(self) -> "str":
        return "sonarqubeserver.svg"

    @property
    def title(self) -> "str":
        return "SonarQube Server"

    @property
    def primary_color(self) -> "str":
        return "#126ED3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SonarQube Server</title>
     <path d="M12 0a.774.774 0 0 0-.775.775c0 .43.346.776.775.776
 5.762 0 10.45 4.687 10.45 10.449 0 .43.345.775.775.775A.774.774 0 0 0
 24 12c0-6.616-5.384-12-12-12zm0 3.932a.774.774 0 0 0-.775.775c0
 .43.346.775.775.775A6.524 6.524 0 0 1 18.518 12c0
 .43.346.775.775.775.43 0 .775-.346.775-.775
 0-4.448-3.62-8.068-8.068-8.068zm0 3.925a.774.774 0 0 0-.775.776c0
 .43.346.775.775.775A2.597 2.597 0 0 1 14.592 12c0
 .43.346.775.775.775.43 0 .776-.346.776-.775A4.145 4.145 0 0 0 12
 7.857zM.775 11.225A.774.774 0 0 0 0 12c0 6.616 5.384 12 12 12 .43 0
 .775-.346.775-.775a.774.774 0 0 0-.775-.776C6.238 22.45 1.55 17.762
 1.55 12a.774.774 0 0 0-.775-.775zm3.932 0a.774.774 0 0 0-.775.775c0
 4.448 3.62 8.068 8.068 8.068.43 0 .775-.346.775-.775a.774.774 0 0
 0-.775-.775A6.524 6.524 0 0 1 5.482 12a.774.774 0 0
 0-.775-.775zm3.926 0a.774.774 0 0 0-.776.775A4.145 4.145 0 0 0 12
 16.143c.43 0 .775-.347.775-.776a.774.774 0 0 0-.775-.775A2.597 2.597
 0 0 1 9.408 12a.774.774 0 0 0-.775-.775z" />
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
