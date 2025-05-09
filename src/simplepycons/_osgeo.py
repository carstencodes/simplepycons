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


class OsgeoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "osgeo"

    @property
    def original_file_name(self) -> "str":
        return "osgeo.svg"

    @property
    def title(self) -> "str":
        return "OSGeo"

    @property
    def primary_color(self) -> "str":
        return "#4CB05B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OSGeo</title>
     <path d="M11.38742 0 9.88227 2.63735c-4.10198.91912-7.20472
 4.44855-7.4712 8.7637h2.41025c.29326-3.50262 3.07658-6.28647
 6.5661-6.57945V2.42416Zm1.21236 2.41136V4.8216c3.48923.29298 6.27256
 3.0763 6.56554
 6.56554H23.99972l-2.6368-1.50459c-.91883-4.10198-4.44798-7.205-8.76314-7.4712Zm-.61286
 3.28917-.7459 4.55497 1.4918.9986.9986 1.4918
 4.55497-.75926-4.55497-.7459 1.97106-2.95685-2.9563 1.9716zm.7459
 5.55358L8.28415 8.28443l2.97022 4.4481 4.4481 2.97021zm-1.47844
 1.47843-.99916-1.49124L5.7008 12l4.5544.7459-1.97105 2.95685
 2.9435-1.97105.75926 4.55441.7587-4.55441zm.73254-1.26524c.27958 0
 .51934.23976.51934.51934 0
 .27987-.22636.5199-.51934.5199s-.51935-.24003-.51935-.5199c0-.29298.23976-.51934.51935-.51934zM.00028
 12.5995l2.63735 1.5046c.91912 4.10226 4.44799 7.20555 8.76315
 7.47174v-2.4108c-3.50263-.29298-6.28593-3.0763-6.5789-6.56554H2.42444Zm19.16504
 0c-.29298 3.48923-3.0763 6.27256-6.56554
 6.56554V24l1.5046-2.63735c4.10197-.91883 7.20527-4.448
 7.47174-8.76315z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.osgeo.org/about/branding-material'''
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
