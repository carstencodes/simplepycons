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


class FreetubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freetube"

    @property
    def original_file_name(self) -> "str":
        return "freetube.svg"

    @property
    def title(self) -> "str":
        return "FreeTube"

    @property
    def primary_color(self) -> "str":
        return "#F04242"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FreeTube</title>
     <path d="M4.7066 0c.9 0 1.6294.7295 1.6294
 1.6294V24H4.0993a4.0988 4.0988 0 0 1-2.8986-1.2007A4.0988 4.0988 0 0
 1 0 19.9007V1.6294C0 .7294.7295 0 1.6294 0ZM24 0v1.9409a4.3951 4.3951
 0 0 1-4.3951 4.3951H9.0053c-.891
 0-1.6133-.7223-1.6133-1.6133V1.6133C7.392.7223 8.1143 0 9.0053
 0Zm-6.7817 11.734a.618.618 0 0 1 0 1.108l-8.9022 4.412a.64.64 0 0
 1-.9241-.5734V7.8954a.64.64 0 0 1 .9241-.5734Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/FreeTubeApp/FreeTube/blob/'''

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
