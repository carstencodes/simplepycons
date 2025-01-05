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


class OpenstackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openstack"

    @property
    def original_file_name(self) -> "str":
        return "openstack.svg"

    @property
    def title(self) -> "str":
        return "OpenStack"

    @property
    def primary_color(self) -> "str":
        return "#ED1944"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenStack</title>
     <path d="M18.575 9.29h5.418v5.42h-5.418zM0
 9.29h5.419v5.42H0zm18.575 7.827a1.207 1.207 0 0 1-1.206
 1.206H6.623a1.207 1.207 0 0 1-1.205-1.206v-.858H0v5.252a2.236 2.236 0
 0 0 2.229 2.23h19.53A2.237 2.237 0 0 0 24
 21.512V16.26h-5.425zM21.763.258H2.233a2.236 2.236 0 0 0-2.23
 2.23V7.74h5.419v-.858a1.206 1.206 0 0 1 1.205-1.206h10.746a1.206
 1.206 0 0 1 1.205 1.206v.858H24V2.487A2.237 2.237 0 0 0 21.763.258Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.openstack.org/brand/openstack-log'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.openstack.org/brand/openstack-log'''

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
